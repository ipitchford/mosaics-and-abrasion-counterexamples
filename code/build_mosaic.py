#!/usr/bin/env python3
"""Build an exact rational counterexample to the 3D harmonic-degree band.

No convex-hull floating point routine is used. The 4-polytope is the n=6,
epsilon=1/2 projected deformed cube of Joswig--Ziegler. Positive circuits
in the two eliminated coordinates enumerate its facets. Two stackings
supply a tetrahedral Schlegel boundary. All arithmetic is rational.
"""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("Run without -O: exact verification assertions must remain enabled.")
from fractions import Fraction as F
from itertools import product, combinations
from math import comb, gcd, lcm
from pathlib import Path
import argparse, json
import sympy as sp


def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def avg(vs): return tuple(sum((v[j] for v in vs),F(0))/len(vs) for j in range(len(vs[0])))
def rank(vs):
    if not vs:return -1
    return sp.Matrix([[sp.Rational(x-y) for x,y in zip(v,vs[0])] for v in vs[1:]]).rank()
def primitive(xs):
    den=lcm(*(x.denominator for x in xs));z=[int(x*den) for x in xs]
    g=gcd(*z);return tuple(F(x//g) for x in z)
def plane(vs, vertices):
    ns=sp.Matrix([[sp.Rational(x) for x in v]+[1] for v in vs]).nullspace()
    assert len(ns)==1
    h=primitive(tuple(F(x) for x in ns[0]));values=[dot(h[:-1],v)+h[-1] for v in vertices]
    if max(values)>0:h=tuple(-x for x in h);values=[-x for x in values]
    assert max(values)==0 and min(values)<0
    return h

def initial_polytope():
    n=6;eps=F(1,2);vertices=[];signs=list(product((-1,1),repeat=n))
    scales=[F(2**(k*(k+1)//2)) for k in range(3,7)]
    for sig in signs:
        x=[]
        for k in range(1,n+1):
            rhs=F(2**comb(k,2))/eps**(k-1)
            if k>1:rhs-=(-1)**k*sum((F(comb(k-2,j-1))*x[j-1] for j in range(1,k)),F(0))
            assert rhs>0
            x.append(sig[k-1]*rhs/eps)
        vertices.append(tuple(x[j+2]/scales[j] for j in range(4)))
    rows=[]
    for k in range(1,n+1):
        for sig in (-1,1):
            a=[F(0)]*n
            for j in range(1,k):a[j-1]=F((-1)**k*comb(k-2,j-1))
            a[k-1]=sig*eps
            rows.append((k-1,sig,a,F(2**comb(k,2))/eps**(k-1)))
    facets=[];circuits=[];planes=[]
    for ids in combinations(range(12),3):
        rr=[rows[i] for i in ids]
        if len({r[0] for r in rr})<3:continue
        u=[r[2][:2] for r in rr]
        det=lambda a,b:a[0]*b[1]-a[1]*b[0]
        coeff=[det(u[1],u[2]),det(u[2],u[0]),det(u[0],u[1])]
        if all(x<0 for x in coeff):coeff=[-x for x in coeff]
        if not all(x>0 for x in coeff):continue
        ids_v=[i for i,s in enumerate(signs) if all(s[r[0]]==r[1] for r in rr)]
        assert len(ids_v)==8 and rank([vertices[i] for i in ids_v])==3
        a=[sum((c*r[2][j] for c,r in zip(coeff,rr)),F(0)) for j in range(6)]
        b=sum((c*r[3] for c,r in zip(coeff,rr)),F(0))
        assert a[:2]==[0,0]
        h=primitive(tuple(a[j+2]*scales[j] for j in range(4))+(-b,))
        assert all(dot(h[:-1],v)+h[-1]<=0 for v in vertices)
        assert set(ids_v)=={i for i,v in enumerate(vertices) if dot(h[:-1],v)+h[-1]==0}
        facets.append(tuple(ids_v));planes.append(h)
        circuits.append({'rows':list(ids),'coefficients':list(map(str,coeff))})
    order=sorted(range(len(facets)),key=lambda i:facets[i])
    facets=[facets[i] for i in order];planes=[planes[i] for i in order];circuits=[circuits[i] for i in order]
    assert len(vertices)==64 and len(facets)==64 and len(set(facets))==64
    return vertices,facets,planes,circuits

def beyond(vertices, facets, hs, index):
    z=avg([vertices[i] for i in facets[index]]);w=avg(vertices);d=tuple(a-b for a,b in zip(z,w))
    delta=F(1,2)
    for j,h in enumerate(hs):
        if j==index:continue
        slack=-(dot(h[:-1],z)+h[-1]);slope=dot(h[:-1],d)
        assert slack>0
        if slope>0:
            while delta*slope>=slack:delta/=2
    p=tuple(a+delta*b for a,b in zip(z,d))
    vals=[dot(h[:-1],p)+h[-1] for h in hs]
    assert vals[index]>0 and all(x<0 for j,x in enumerate(vals) if j!=index)
    return p,delta

def stack(vertices, facets, hs, index):
    p,delta=beyond(vertices,facets,hs,index);target=set(facets[index]);ridges=set()
    for j,g in enumerate(facets):
        if j==index:continue
        ints=tuple(sorted(target.intersection(g)))
        if len(ints)>=3 and rank([vertices[i] for i in ints])==2:ridges.add(ints)
    newverts=vertices+[p];newfacets=[f for j,f in enumerate(facets) if j!=index]
    newfacets += [tuple(sorted(r+(len(vertices),))) for r in sorted(ridges)]
    newfacets.sort();newhs=[plane([newverts[i] for i in f],newverts) for f in newfacets]
    log={'removed_facet':facets[index], 'point':list(map(str,p)), 'delta':str(delta), 'ridges':list(sorted(ridges)), 'new_facet_count':len(newfacets)}
    return newverts,newfacets,newhs,log

def schlegel(vertices, facets, hs, index):
    view,delta=beyond(vertices,facets,hs,index);h=hs[index]
    s=dot(h[:-1],view)+h[-1];boundary=facets[index];assert len(boundary)==4
    mat=sp.Matrix([[sp.Rational(vertices[i][j]) for i in boundary] for j in range(4)]+[[1]*4])
    rows=next(rs for rs in combinations(range(5),4) if mat[list(rs),:].det()!=0)
    inv=mat[list(rows),:].inv();points=[];heights=[]
    for p in vertices:
        gap=-(dot(h[:-1],p)+h[-1]);t=s/(s+gap)
        y=tuple(view[j]+t*(p[j]-view[j]) for j in range(4))+(F(1),)
        lam=inv*sp.Matrix([sp.Rational(y[j]) for j in rows]);lam=tuple(F(x) for x in lam)
        assert sum(lam)==1 and min(lam)>=0
        points.append(lam[1:]);heights.append(t-1)
    assert sum(1 for p in points if min((1-sum(p),)+p)>0)==len(vertices)-4
    cells=[f for j,f in enumerate(facets) if j!=index]
    return points,heights,cells,{'outer_facet':boundary,'viewpoint':list(map(str,view)),'delta':str(delta),'outer_plane':list(map(str,h))}

def build(out):
    verts,facets,hs,circuits=initial_polytope()
    initial={'vertices':[[str(x) for x in p] for p in verts], 'facets':facets, 'halfspaces':[[str(x) for x in h] for h in hs], 'circuits':circuits}
    verts,facets,hs,step1=stack(verts,facets,hs,0)
    target=next(i for i,f in enumerate(facets) if len(f)==5 and 64 in f)
    verts,facets,hs,step2=stack(verts,facets,hs,target)
    assert len(verts)==66 and len(facets)==73 and sum(map(len,facets))==550
    target=next(i for i,f in enumerate(facets) if len(f)==4 and 65 in f)
    points,heights,cells,proj=schlegel(verts,facets,hs,target)
    V=1+6*(len(points)-4);C=6*len(cells);I=6*sum(map(len,cells))
    data={'schema':'evidence-press/problem2/rational-mosaic/v1','initial':initial,'stackings':[step1,step2],
          'polytope':{'vertices':[[str(x) for x in p] for p in verts], 'facets':facets, 'halfspaces':[[str(x) for x in h] for h in hs]},
          'projection':proj,'template':{'vertices':[[str(x) for x in p] for p in points], 'regular_heights':list(map(str,heights)),'cells':cells},
          'periodic_counts':{'V':V,'C':C,'I':I,'mean_cells_per_vertex':str(F(I,V)),'mean_vertices_per_cell':str(F(I,C)),'harmonic_degree':str(F(I,V+C))},
          'periodic_rule':'For each z in Z^3 and permutation pi of (0,1,2), map the ordered outer tetrahedron to z, z+e_pi[0], z+e_pi[0]+e_pi[1], z+(1,1,1).'}
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'certificate':str(out),**data['periodic_counts']},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parents[1]/'evidence'/'mosaic_certificate.json');args=parser.parse_args();build(args.output)
