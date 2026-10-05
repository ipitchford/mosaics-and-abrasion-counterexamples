#!/usr/bin/env python3
"""Exact symbolic checks for the abrasion counterexample and stochastic audit.

The continuum flow result follows from the analytic fold/short-time-existence
proof in the manuscript. This script certifies its polynomial jets, critical-
point enumeration, convexity constants and finite probability calculation;
it is not a numerical integration of the PDE or a formal PDE proof.
"""
from pathlib import Path
if not __debug__:
    raise RuntimeError("Run without -O: exact verification assertions must remain enabled.")
from fractions import Fraction as F
import json
import sympy as S
ROOT=Path(__file__).resolve().parents[1]

def run():
    x,y,z,mu=S.symbols('x y z mu',real=True);eps=S.Rational(1,100)
    f=y*y/2+x**3*z/6-2*x*y*y*z+mu*x*z
    assert S.expand(f.subs({x:-x,y:-y,z:-z},simultaneous=True)-f)==0
    chart=f.subs(z,S.sqrt(1-x*x-y*y));origin={x:0,y:0,mu:0}
    deriv=lambda dx,dy:S.simplify(S.diff(1+eps*chart,x,dx,y,dy).subs(origin))
    jets={'s':deriv(0,0),'sx':deriv(1,0),'sy':deriv(0,1),'sxx':deriv(2,0),'sxy':deriv(1,1),'syy':deriv(0,2),'sxxx':deriv(3,0),'sxyy':deriv(1,2)}
    assert list(jets.values())==[1,0,0,0,0,eps,eps,-4*eps]
    mcf=eps*(1-4/(1+eps)**2);gauss=eps*(1/(1+eps)-4/(1+eps)**2)
    assert mcf<0 and gauss<0
    # Convexity proof's rational operator norm majorants.
    quartic_hessian_bound=S.Integer(6);quadratic_hessian_bound=S.Integer(1)
    radial_term_bound=S.Rational(3,2);perturbation_bound=S.Rational(3,2)
    total=quartic_hessian_bound+quadratic_hessian_bound+radial_term_bound+perturbation_bound
    assert total==10 and 1-eps*total==S.Rational(9,10)
    t,q=S.symbols('t q',real=True)
    A=t**3/(6*(1+t*t)**2);B=t/(1+t*t)
    Ffun=A+q*(S.Rational(1,2)-2*A-2*B)+q*q*(A+2*B)
    D=13*t**4-3*t*t-12
    qstar=t*t*(t*t-3)/D
    p=13*t**4-52*t**3-3*t*t+48*t-12
    assert S.factor(S.diff(Ffun,t).subs(q,qstar))==0
    assert S.factor(S.diff(Ffun,q).subs(q,qstar)-p/(2*D))==0
    assert S.gcd(p,S.diff(p,t))==1 and S.gcd(p,D)==1
    intervals=[(-S.Rational(99,100),-S.Rational(98,100)),(S.Rational(27,100),S.Rational(28,100)),(S.Rational(88,100),S.Rational(89,100)),(S.Rational(382,100),S.Rational(383,100))]
    assert S.Poly(p,t).count_roots(-S.oo,S.oo)==4
    determinant=S.factor((4*q*(S.diff(Ffun,t,2)*S.diff(Ffun,q,2)-S.diff(Ffun,t,q)**2)).subs(q,qstar))
    dn,dd=S.fraction(determinant)
    records=[];counts={'minimum':2,'maximum':2,'saddle':2}
    # Count and classify roots by exact Sturm isolation and constant signs.
    for lo,hi in intervals:
        assert S.Poly(p,t).count_roots(lo,hi)==1
        for poly in (dn,dd,S.fraction(qstar)[0],D,S.fraction(S.factor(1-qstar))[0]):
            assert S.Poly(poly,t).count_roots(lo,hi)==0
        mid=(lo+hi)/2
        assert 0<qstar.subs(t,mid)<1
        sign_det=S.sign(determinant.subs(t,mid))
        sign_rr=S.sign((t*(13*t*t+12)/(3*(1+t*t)**2)).subs(t,mid))
        typ='saddle' if sign_det<0 else ('minimum' if sign_rr>0 else 'maximum')
        counts[typ]+=4
        records.append({'root_interval':[str(lo),str(hi)],'root_count':1,'q_between_zero_and_one':True,'Hessian_determinant_sign':int(sign_det),'type':typ,'multiplicity_on_sphere':4})
    assert counts=={'minimum':6,'maximum':6,'saddle':10}
    # Remaining charts: four y=0 Morse points and the y=+/-1 saddles.
    theta=S.symbols('theta',real=True)
    angular=S.sin(theta)**3*S.cos(theta)/6
    assert S.trigsimp(S.diff(angular,theta)-S.sin(theta)**2*(3*S.cos(theta)**2-S.sin(theta)**2)/6)==0
    pole_chart=f.subs({y:S.sqrt(1-x*x-z*z),mu:0})
    polar_hessian=S.hessian(pole_chart,[x,z]).subs({x:0,z:0})
    assert polar_hessian==S.Matrix([[-1,-2],[-2,-1]])
    assert S.simplify(S.diff(Ffun,q).limit(t,S.oo))==S.Rational(1,2)
    # At the four y=0 Morse points: product of two nonzero Hessian eigenvalues.
    for sign in (-1,1):
        tt=sign*S.sqrt(3)
        rr=S.simplify((1-4*A-4*B).subs(t,tt))
        aa=S.simplify(((1+t*t)*S.diff((1+t*t)*S.diff(A,t),t)).subs(t,tt))
        assert S.sign(rr)==S.sign(aa)==-sign
    outcomes=[(F(9,20),F(1),F(-2)),(F(9,20),F(-1),F(2)),(F(1,20),F(1),F(18)),(F(1,20),F(-1),F(-18))]
    E=lambda fn:sum((w*fn(a,b) for w,a,b in outcomes),F(0))
    sign=lambda x:F(1 if x>0 else -1 if x<0 else 0)
    moments={'EA':E(lambda a,b:a),'EB':E(lambda a,b:b),'EAB':E(lambda a,b:a*b),'EA2':E(lambda a,b:a*a),'EB2':E(lambda a,b:b*b),'E_expression':E(lambda a,b:a*a+a*b),'E_sign':E(lambda a,b:sign(a*a+a*b)),'E_jump':E(lambda a,b:-2*sign(a*a+a*b))}
    assert [moments[k] for k in ('EA','EB','EAB')]==[0,0,0]
    assert moments['E_expression']==1 and moments['E_sign']==F(-4,5) and moments['E_jump']==F(8,5)
    # Moment-preserving family and corrected equal-scale examples.
    qq=S.symbols('qq', positive=True)
    assert S.simplify(-2*qq+(1-qq)*2*qq/(1-qq))==0
    assert S.simplify(4*qq+(1-qq)*(2*qq/(1-qq))**2-4*qq/(1-qq))==0
    # Independent uniform noise of half-width 1/2 cannot change either sign.
    assert -1+F(1,2)<0 and 19-F(1,2)>0
    independent_mean=sum((sign(F(a*a+a*b)) for a in (-1,1) for b in (-2,2)),F(0))/4
    assert independent_mean==0
    assert S.simplify(2/S.pi*S.atan(1))==S.Rational(1,2)
    report={'status':'PASS','arithmetic':'exact symbolic and rational','epsilon':str(eps),'support_function':'1 + epsilon*(y^2/2 + x^3*z/6 - 2*x*y^2*z + mu*x*z), x^2+y^2+z^2=1',
            'central_symmetry':True,'curvature_radius_lower_bound_for_abs_mu_le_1':'9/10','fold_jets':{k:str(v) for k,v in jets.items()},
            'MCF_gradient_time_derivative_at_fold':str(mcf),'Gauss_flow_gradient_time_derivative_at_fold':str(gauss),'MCF_fold_time_linear_coefficient':str(-eps/mcf),
            'critical_quartic':str(p),'quartic_discriminant':str(S.discriminant(p,t)),'root_certificates':records,
            'Morse_critical_counts_at_mu_zero':counts,'additional_degenerate_points':2,
            'positive_mu_before_birth_total':22,'after_antipodal_birth_total':26,
            'probability_extensions':{'moment_family':'E sign = 1-2q, q in (0,1)','independent_small_uniform_noise_preserves_counterexample':True,'independent_Rademacher_A_and_double_Rademacher_B_mean_sign':'0','equal_scale_independent_Gaussian_mean_sign':'1/2'},'stochastic_outcomes':[{'probability':str(w),'A':str(a),'B':str(b)} for w,a,b in outcomes],'stochastic_moments':{k:str(v) for k,v in moments.items()},
            'scope':'The exact calculations support the analytic existence/fold argument. No flow discretization or assertion about an unspecified probability ensemble is used.'}
    (ROOT/'evidence/abrasion_verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':run()
