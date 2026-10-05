#!/usr/bin/env python3
"""Independent exact verification of the rational mosaic certificate.

Uses Fraction/SymPy, not the builder and not a floating-point hull library.
It checks elimination completeness, all supports, the complete face lattices,
Schlegel geometry, local gluing, regularity and exact total volume.
"""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("Run without -O: exact verification assertions must remain enabled.")
import argparse, json, sys, hashlib, time
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
from pathlib import Path
import sympy as S


def dot(x,y): return sum((a*b for a,b in zip(x,y)),F(0))
def bary(vs): return tuple(sum((p[k] for p in vs),F(0))/len(vs) for k in range(len(vs[0])))
def arank(vs):
    if not vs:return -1
    if len(vs)==1:return 0
    return S.Matrix([[S.Rational(a-b) for a,b in zip(p,vs[0])] for p in vs[1:]]).rank()
def rat(x):return F(x)
def det3(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def check_supports(vs,fs,hs):
    assert len(fs)==len(hs) and arank(vs)==4
    assert len(set(vs))==len(vs)
    for face,h in zip(fs,hs):
        values=[dot(h[:-1],p)+h[-1] for p in vs]
        assert max(values)==0 and min(values)<0
        assert frozenset(i for i,v in enumerate(values) if v==0)==face
        assert arank([vs[i] for i in face])==3
    for i in range(len(vs)):
        normals=[list(h[:-1]) for f,h in zip(fs,hs) if i in f]
        assert S.Matrix(normals).rank()==4

def lattice(vs,fs):
    faces={frozenset(range(len(vs)))}
    for facet in fs:
        faces |= {f & facet for f in tuple(faces)}
    ranks={f:arank([vs[i] for i in sorted(f)]) for f in faces}
    counts=Counter(ranks.values())
    assert counts[-1]==1 and counts[4]==1 and counts[0]==len(vs)
    assert counts[3]==len(fs)
    assert counts[0]-counts[1]+counts[2]-counts[3]==0
    for ridge,r in ranks.items():
        if r==2:assert sum(ridge<=f for f in fs)==2
    return ranks,[counts[i] for i in range(4)]

def check_elimination(vs,fs):
    # Reconstruct all vertices of the triangularly deformed 6-cube.
    scales=[2**(k*(k+1)//2) for k in range(3,7)]
    rebuilt=[]
    for sign in product((-1,1),repeat=6):
        x=[]
        for k in range(1,7):
            c=F(2**comb(k,2))*2**(k-1)
            if k>1:c-=(-1)**k*sum(F(comb(k-2,j-1))*x[j-1] for j in range(1,k))
            assert c>0
            x.append(2*sign[k-1]*c)
        rebuilt.append(tuple(x[k+2]/scales[k] for k in range(4)))
    assert rebuilt==vs
    rows=[]
    for k in range(1,7):
        for sign in (-1,1):
            a=[F(0)]*6
            for j in range(1,k):a[j-1]=F((-1)**k*comb(k-2,j-1))
            a[k-1]=F(sign,2)
            rows.append((a,F(2**comb(k,2))*2**(k-1)))
    # Extreme nonnegative dependencies in two dimensions have support <=3.
    ray_count=0;genuine=set();degenerate=0;rank_hist=Counter()
    for size in (1,2,3):
        for ids in combinations(range(12),size):
            mat=S.Matrix([[rows[i][0][k] for i in ids] for k in (0,1)])
            ns=mat.nullspace()
            if len(ns)!=1:continue
            v=[F(t) for t in ns[0]]
            if all(t<0 for t in v):v=[-t for t in v]
            if not all(t>0 for t in v):continue
            ray_count+=1
            a=[sum((c*rows[i][0][k] for c,i in zip(v,ids)),F(0)) for k in range(6)]
            b=sum((c*rows[i][1] for c,i in zip(v,ids)),F(0))
            assert a[0]==a[1]==0
            hp=[a[k+2]*scales[k] for k in range(4)]
            vals=[dot(hp,p)-b for p in vs]
            assert max(vals)<=0
            equal=frozenset(i for i,t in enumerate(vals) if t==0)
            dim=arank([vs[i] for i in equal]);rank_hist[dim]+=1
            if dim==3:genuine.add(equal)
            else:degenerate+=1
    assert genuine==set(fs)
    return {'positive_circuit_rays':ray_count,'facet_defining_rays':len(genuine),'other_rays':degenerate,'equality_rank_histogram':dict(rank_hist)}

def verify(path,out):
    started=time.time();d=json.loads(path.read_text())
    decode=lambda o:([tuple(map(F,p)) for p in o['vertices']], [frozenset(f) for f in o['facets']], [tuple(map(F,h)) for h in o['halfspaces']])
    v0,f0,h0=decode(d['initial']);check_supports(v0,f0,h0)
    elimination=check_elimination(v0,f0)
    l0,counts0=lattice(v0,f0)
    for facet in f0:
        local=Counter(r for f,r in l0.items() if f<=facet)
        assert [local[i] for i in range(4)]==[8,12,6,1]
        assert all(len(f)==4 for f,r in l0.items() if r==2 and f<=facet)
    vs,fs,hs=decode(d['polytope']);check_supports(vs,fs,hs)
    ranks,counts=lattice(vs,fs)
    # Replay stacking combinatorics and beyond/beneath inequalities, without invoking builder.
    oldv,oldf,oldh=v0,f0,h0
    for step in d['stackings']:
        target=frozenset(step['removed_facet']);p=tuple(map(F,step['point']))
        assert target in oldf
        for face,h in zip(oldf,oldh):
            value=dot(h[:-1],p)+h[-1]
            assert value>0 if face==target else value<0
        rr={target&f for f in oldf if f!=target and arank([oldv[i] for i in target&f])==2}
        assert rr=={frozenset(r) for r in step['ridges']}
        oldf=[f for f in oldf if f!=target]+[r|{len(oldv)} for r in rr]
        oldv=oldv+[p]
        oldh=[]
        for face in oldf:
            ns=S.Matrix([[*oldv[i],1] for i in face]).nullspace();assert len(ns)==1
            h=tuple(F(t) for t in ns[0]);values=[dot(h[:-1],x)+h[-1] for x in oldv]
            if max(values)>0:h=tuple(-t for t in h)
            oldh.append(h)
        check_supports(oldv,oldf,oldh)
    assert oldv==vs and set(oldf)==set(fs)
    assert counts0==[64,192,192,64]
    assert counts==[66,205,212,73]
    # Validate projection and lower-hull realization.
    outer=frozenset(d['projection']['outer_facet']);eye=tuple(map(F,d['projection']['viewpoint']))
    assert outer in fs and len(outer)==4
    oh=hs[fs.index(outer)];s=dot(oh[:-1],eye)+oh[-1];assert s>0
    assert all(dot(h[:-1],eye)+h[-1]<0 for f,h in zip(fs,hs) if f!=outer)
    pts=[tuple(map(F,p)) for p in d['template']['vertices']]
    ht=list(map(F,d['template']['regular_heights']));cells=[frozenset(c) for c in d['template']['cells']]
    assert set(cells)==set(fs)-{outer}
    order=d['projection']['outer_facet']
    assert set(pts[i] for i in outer)=={(F(0),F(0),F(0)),(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1))}
    for i,(p,y) in enumerate(zip(vs,pts)):
        lam=(1-sum(y),)+y;assert sum(lam)==1 and min(lam)>=0
        assert (min(lam)>0)==(i not in outer)
        gap=-(dot(oh[:-1],p)+oh[-1]);t=s/(s+gap)
        projected=tuple(eye[k]+t*(p[k]-eye[k]) for k in range(4))
        reconstructed=tuple(sum(lam[j]*vs[order[j]][k] for j in range(4)) for k in range(4))
        assert reconstructed==projected and ht[i]==t-1
    # Every cell is a strict lower face of the supplied rational lifting.
    lifts=[p+(height,) for p,height in zip(pts,ht)]
    for c in cells:
        ns=S.Matrix([[*lifts[i],1] for i in c]).nullspace();assert len(ns)==1
        h=tuple(F(x) for x in ns[0]);assert h[3]!=0
        if h[3]>0:h=tuple(-x for x in h)
        values=[dot(h[:-1],p)+h[-1] for p in lifts]
        assert max(values)==0 and {i for i,x in enumerate(values) if x==0}==set(c)
    # Polygonal face incidences; triangulate by face and cell barycentres.
    faces2=[f for f,r in ranks.items() if r==2]
    edges=[f for f,r in ranks.items() if r==1]
    face_mult=Counter();volumes=[]
    for c in cells:
        cc=bary([pts[i] for i in c]);vol=F(0)
        for face in faces2:
            if not face<=c:continue
            face_mult[face]+=1;fc=bary([pts[i] for i in face])
            face_edges=[e for e in edges if e<=face]
            assert len(face_edges)==len(face)
            for edge in face_edges:
                i,j=sorted(edge)
                volume=abs(det3(sub(fc,cc),sub(pts[i],cc),sub(pts[j],cc)))/6
                assert volume>0;vol+=volume
        assert vol>0;volumes.append(vol)
    assert sum(volumes,F(0))==F(1,6)
    assert Counter(face_mult.values())==Counter({2:208,1:4})
    assert all((mult==1)==(face<=outer) for face,mult in face_mult.items())
    assert len(pts)-counts[1]+len(face_mult)-len(cells)==1
    V=1+6*(len(pts)-4);C=6*len(cells);I=6*sum(map(len,cells));assert (V,C,I)==(373,432,3276)
    assert F(I,V+C)==F(468,115)>4
    expected={'V':V,'C':C,'I':I,'mean_cells_per_vertex':str(F(I,V)),'mean_vertices_per_cell':str(F(I,C)),'harmonic_degree':str(F(I,V+C))}
    assert expected==d['periodic_counts']
    report={'status':'PASS','arithmetic':'exact rational; no numerical tolerances','certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'initial_f_vector':counts0,'final_f_vector':counts,'elimination':elimination,
            'template':{'vertices':len(pts),'interior_vertices':len(pts)-4,'cells':len(cells),'cell_vertex_incidences':sum(map(len,cells)),'interior_polygon_faces':208,'boundary_triangles':4,'exact_volume':str(sum(volumes,F(0))),'strict_regular_lower_hull':True},
            'periodic':expected,'wall_seconds':round(time.time()-started,3)}
    out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':
    root=Path(__file__).resolve().parents[1]
    p=argparse.ArgumentParser();p.add_argument('--certificate',type=Path,default=root/'evidence'/'mosaic_certificate.json');p.add_argument('--output',type=Path,default=root/'evidence'/'mosaic_verification.json');a=p.parse_args();verify(a.certificate,a.output)
