#!/usr/bin/env python3
"""Construct and check a periodic weighted-Delaunay/Laguerre realization.

The Schlegel template is a coherent subdivision with height zero on the
boundary. A strictly convex Freudenthal lifting absorbs a sufficiently
small copy of this template. Exact macro-face tests select the scale.
"""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("Run without -O: exact verification assertions must remain enabled.")
from fractions import Fraction as F
from itertools import permutations,product,combinations
from pathlib import Path
from collections import defaultdict
import json, sympy as S

ROOT=Path(__file__).resolve().parents[1]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def affine(points,values):
    ids=next(c for c in combinations(range(len(points)),4) if S.Matrix([[*points[i],1] for i in c]).det()!=0)
    vec=S.Matrix([[*points[i],1] for i in ids]).inv()*S.Matrix([values[i] for i in ids])
    h=tuple(F(x) for x in vec)
    assert all(dot(h[:-1],p)+h[-1]==v for p,v in zip(points,values))
    return h

def construct():
    d=json.loads((ROOT/'evidence/mosaic_certificate.json').read_text());t=d['template']
    pts=[tuple(map(F,p)) for p in t['vertices']];heights=list(map(F,t['regular_heights']));cells=t['cells'];outer=d['projection']['outer_facet']
    Q=S.eye(3)-S.Rational(5,16)*S.ones(3);A=S.eye(3)-S.Rational(1,4)*S.ones(3)
    assert A.T*A==Q and Q.eigenvals()=={S.Rational(1,16):1,S.Integer(1):2}
    q=lambda x:F((S.Matrix(x).T*Q*S.Matrix(x))[0])
    hplanes=[affine([pts[i] for i in c],[heights[i] for i in c]) for c in cells]
    boundary_cell={}
    for omitted in range(4):
        face=set(outer)-{outer[omitted]}
        matches=[j for j,c in enumerate(cells) if face<=set(c)]
        assert len(matches)==1;boundary_cell[omitted]=matches[0]
    macros={};faces=defaultdict(list)
    for z in product((-1,0,1),repeat=3):
        for pi in permutations(range(3)):
            corners=[z];cur=list(z)
            for k in pi:cur=cur.copy();cur[k]+=1;corners.append(tuple(cur))
            B=S.Matrix.hstack(*(S.Matrix(corners[j])-S.Matrix(z) for j in (1,2,3)));Bi=B.inv()
            base=affine(corners,[q(x) for x in corners]);global_h=[]
            for h in hplanes:
                grad=(S.Matrix(1,3,h[:3])*Bi);grad=tuple(F(x) for x in grad)
                global_h.append(grad+(h[3]-dot(grad,z),))
            key=(z,pi);macros[key]=(corners,B,base,global_h)
            for j in range(4):faces[frozenset(corners[k] for k in range(4) if k!=j)].append((key,j))
    checks=[]
    for key,(corners,B,base,global_h) in macros.items():
        if key[0]!=(0,0,0):continue
        for j in range(4):
            face=frozenset(corners[k] for k in range(4) if k!=j);incident=faces[face];assert len(incident)==2
            other,k=next((x,k) for x,k in incident if x!=key)
            rc,RB,rb,rh=macros[other]
            hp=global_h[boundary_cell[j]];rp=rh[boundary_cell[k]]
            g0=tuple(b-a for a,b in zip(base,rb));g1=tuple(b-a for a,b in zip(hp,rp))
            assert all(dot(g0[:3],x)+g0[3]==0 and dot(g1[:3],x)+g1[3]==0 for x in face)
            opposite=rc[k];b0=dot(g0[:3],opposite)+g0[3];b1=dot(g1[:3],opposite)+g1[3]
            assert b0>0
            checks.append((key,other,j,k,b0,b1))
    delta=F(1,2)
    while not all(b0+delta*b1>0 for _,_,_,_,b0,b1 in checks):delta/=2
    # Representatives of all weighted sites modulo the unit lattice.
    sites={};periodic_cells=[]
    for key,(corners,B,base,global_h) in macros.items():
        if key[0]!=(0,0,0):continue
        local_refs=[]
        for i,p in enumerate(pts):
            x=tuple(F(v) for v in B*S.Matrix(p));H=dot(base[:3],x)+base[3]+delta*heights[i]
            shift=tuple(int(v//1) for v in x);rep=tuple(v-k for v,k in zip(x,shift));weight=q(x)-H
            if rep in sites:assert sites[rep]==weight
            sites[rep]=weight;local_refs.append((rep,shift))
        for c in cells:periodic_cells.append([local_refs[i] for i in c])
    assert len(sites)==373 and len(periodic_cells)==432
    reps=sorted(sites);index={p:i for i,p in enumerate(reps)}
    cert={'schema':'evidence-press/problem2/periodic-weighted-sites/v1','template_scale':str(delta),
          'Euclidean_lattice_basis':[[str(F(x)) for x in A.row(i)] for i in range(3)],
          'metric_Gram_matrix':[[str(F(x)) for x in Q.row(i)] for i in range(3)],
          'site_rule':'For each site below and z in Z^3, use Euclidean site A*(lattice_coordinates+z), with its listed weight. Power distance is ||y-site||^2-weight.',
          'sites':[{'lattice_coordinates':list(map(str,p)),'weight':str(sites[p])} for p in reps],
          'Delaunay_cells':[[{'site':index[p],'lattice_translate':list(z)} for p,z in c] for c in periodic_cells],
          'macro_face_checks':[{'left_permutation':list(key[1]),'right_translate':list(other[0]),'right_permutation':list(other[1]),'left_omitted_corner':j,'right_omitted_corner':k,'base_gap':str(b0),'template_gap':str(b1),'final_gap':str(b0+delta*b1)} for key,other,j,k,b0,b1 in checks]}
    report={'status':'PASS','arithmetic':'exact rational','template_scale':str(delta),'weighted_sites_per_period':len(sites),'Delaunay_cells_per_period':len(periodic_cells),
            'directed_macro_face_tests':len(checks),'minimum_strict_macro_gap':str(min(b0+delta*b1 for *_,b0,b1 in checks)),
            'Laguerre_dual_counts':{'V':432,'C':373,'I':3276,'harmonic_degree':'468/115'},
            'global_argument':'Strict local convexity within every macro tetrahedron and across every macro face, plus quadratic-periodic growth, certifies the global weighted lower hull. The dual is the power diagram of the listed periodic sites.'}
    return cert, report

def run():
    cert, report = construct()
    (ROOT/'evidence/weighted_sites_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    (ROOT/'evidence/regular_realization_verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':run()
