<div class="center">

Unrefereed candidate. DOI: <https://doi.org/10.5281/zenodo.23167004>

</div>

**Keywords.** Geometric abrasion; mean-curvature flow; support function;
static equilibrium; saddle-node bifurcation; covariance; stochastic
drift.

# The two statements must be separated

The supplied geology problem bundle asks whether the number of static
equilibria, measured from a convex body’s centroid, decreases
monotonically under curvature-driven abrasion. Taken as a universal
deterministic statement, the answer is negative. We prove this using the
exact body family below.

The actual Conjecture 1 of , however, is formulated for the expected
value $`\bar N(t)`$. The same paper already acknowledges that
deterministic spatial critical-point counts can increase on surfaces,
discusses a heat-equation birth example, and studies nonmonotonic
centroidal counts in an illustrative planar model. We do not claim that
the general possibility of creation is new. Our deterministic
contribution is an explicit globally convex three-dimensional centroidal
construction, with all equilibria enumerated and a genuine
curvature-flow birth certified analytically.

The stochastic result in replaces third derivatives by random variables
with zero means and covariance. Its claimed sign inference does not
follow from those moments.
Section <a href="#sec:probability" data-reference-type="ref"
data-reference="sec:probability">6</a> gives an exact counterexample and
replacement conditions. This invalidates the moment-based drift
conclusion, not every possible stochastic model of abrasion. In
particular, an alternative sampling hypothesis called Assumption 2-A in
that paper is logically distinct and is not refuted by our four-outcome
law.

The general local creation mechanism under Gaussian smoothing already
belongs to the scale-space literature, notably . That result is
background, not the theorem claimed here: the present construction
controls a closed strictly convex body’s centroid and enumerates all
equilibria under the actual nonlinear curvature equation. The separate
probability result repairs a moment-to-sign inference; it does not
supply a physical sampling law.

<div id="thm:main" class="theorem">

**Theorem 1** (Explicit centroidal creation). *Put
$`\varepsilon=1/100`$. For $`u=(x,y,z)\in S^2`$, define
``` math
\begin{equation}
\label{eq:support}
 s_\mu(u)=1+\varepsilon f_\mu(u),\qquad
 f_\mu(u)=\frac{y^2}{2}+\frac{x^3z}{6}-2xy^2z+\mu xz.
\end{equation}
```
For $`|\mu|\le1`$, this is the support function of a smooth strictly
convex body with every principal curvature radius at least $`9/10`$. The
homogeneous body’s centroid is the origin. For all sufficiently small
$`\mu>0`$, inward mean-curvature flow starting from this body undergoes
two antipodal saddle-node births at a positive time $`t_*(\mu)`$. In a
neighborhood of this time, away from the bifurcation instant,
``` math
N(t)=22\quad(t<t_*),\qquad N(t)=26\quad(t>t_*),
 \qquad t_*(\mu)=\frac{10201}{29799}\mu+O(\mu^2).
```
The centroid stays fixed throughout the flow. Initially and immediately
before the births there are 6 stable equilibria, 6 unstable equilibria
and 10 saddles; afterwards there are 8 stable equilibria, 6 unstable
equilibria and 12 saddles.*

</div>

The assertion “sufficiently small” is an analytic quantifier proved
below, not a numerical guess at a parameter threshold. The package does
not certify a particular numerical upper bound on $`\mu`$ or integrate
the flow numerically.

# Support geometry and uniform convexity

For a smooth function $`s:S^2\to\mathbb R`$, write
``` math
Q_s=\nabla^2_{S^2}s+sI.
```
When $`s>0`$ and $`Q_s`$ is positive definite, the homogeneous extension
$`\widetilde s(v)=|v|s(v/|v|)`$ is convex: its tangential Hessian is
$`Q_s/|v|`$, its radial Hessian vanishes, and positivity gives convexity
also on lines through the origin. It is therefore a support function.
Its boundary in outward-normal coordinates is
``` math
\begin{equation}
\label{eq:normalparam}
 X(u)=s(u)u+\nabla_{S^2}s(u),\qquad dX=Q_s,
\end{equation}
```
and the eigenvalues of $`Q_s`$ are the principal curvature radii.

<div id="lem:convex" class="lemma">

**Lemma 2**. *For the functions
<a href="#eq:support" data-reference-type="eqref"
data-reference="eq:support">[eq:support]</a>, $`s_\mu>0`$ and
$`Q_{s_\mu}\succeq(9/10)I`$ whenever $`|\mu|\le1`$.*

</div>

<div class="proof">

*Proof.* For the restriction of an ambient polynomial $`f`$ to the unit
sphere,
``` math
Q_f=(D^2 f)|_{u^\perp}+(f-u\cdot\nabla f)I.
```
Set $`f_2=y^2/2`$, $`g=x^3z/6-2xy^2z`$ and $`h=xz`$. The ambient Hessian
of $`g`$ is
``` math
D^2g=\begin{pmatrix}
 xz&-4yz&x^2/2-2y^2\\
 -4yz&-4xz&-4xy\\
 x^2/2-2y^2&-4xy&0
 \end{pmatrix}.
```
On $`S^2`$, its maximum absolute row sum is at most 6, so its operator
norm is at most 6. Also $`\|D^2f_2\|\le1`$ and $`\|D^2h\|=1`$. The
bounds $`|f_2|\le1/2`$, $`|h|\le1/2`$, and
``` math
|g|\le\frac1{12}+\frac14=\frac13
```
follow from $`|xz|\le1/2`$ and $`2|xz|y^2\le(1-y^2)y^2\le1/4`$.
Homogeneity gives
``` math
f_\mu-u\cdot\nabla f_\mu=-f_2-3g-\mu h.
```
Thus
``` math
\|Q_{f_\mu}\|\le 6+1+|\mu|+\frac32+\frac{|\mu|}{2}
 =\frac{17}{2}+\frac32|\mu|\le10.
```
Consequently
$`Q_{s_\mu}=I+\varepsilon Q_{f_\mu}\succeq(1-10\varepsilon)I=(9/10)I`$.
The bound $`|f_\mu|\le4/3`$ also gives $`s_\mu>0`$. ◻

</div>

Every term of $`f_\mu`$ is even under $`u\mapsto-u`$. Hence the body is
centrally symmetric and its homogeneous centroid is zero. It is also
invariant under $`y\mapsto-y`$. Isometry invariance and uniqueness of
the flow preserve both symmetries.

<div id="lem:equilibria" class="lemma">

**Lemma 3** (Equilibrium correspondence). *For a strictly convex body
containing the origin, centroidal static equilibria are exactly the
critical points of its support function, when its centroid is the
origin. Their Morse types agree with those of the radial distance from
the origin.*

</div>

<div class="proof">

*Proof.* A horizontal supporting plane through $`X(u)`$ balances the
body precisely when the normal through the support point passes through
the centroid. By <a href="#eq:normalparam" data-reference-type="eqref"
data-reference="eq:normalparam">[eq:normalparam]</a>, $`X(u)`$ is
parallel to $`u`$ exactly when $`\nabla s=0`$. For the radial-distance
type, differentiate
``` math
|X|^2=s^2+|\nabla s|^2,
 \qquad \nabla(|X|^2)=2Q_s\nabla s.
```
At a critical point the Hessian is $`2Q_s\nabla^2s`$. The factors
commute because $`Q_s=sI+\nabla^2s`$, and $`Q_s`$ is positive definite,
so the Hessians have the same inertia. The Gauss parametrization and
radial parametrization are diffeomorphic, preserving the critical-point
classification. ◻

</div>

# A forward-time fold, not a backward PDE argument

Here mean curvature means the *sum* $`\kappa_1+\kappa_2`$, not its
average. The averaged convention doubles the displayed birth time. For
inward mean-curvature flow, the support equation is
``` math
\begin{equation}
\label{eq:mcf}
 \partial_t s=-\mathop{\mathrm{tr}}(Q_s^{-1}).
\end{equation}
```
Smooth strictly convex initial surfaces have a unique smooth solution
for a positive short time . The following records precisely the local
dependence needed here.

<div id="lem:dependence" class="lemma">

**Lemma 4** (Common forward interval and dependence). *Fix
$`0<\alpha<1`$ and one smooth strictly convex initial support function.
For the mean-curvature equation, or any fixed speed in
Theorem <a href="#thm:bloore" data-reference-type="ref"
data-reference="thm:bloore">5</a>, some $`C^{6,\alpha}(S^2)`$
neighborhood of that function has a common existence interval $`[0,T]`$.
Its solution map is continuous into $`C([0,T];C^2(S^2))`$. For a smooth
finite-dimensional family of smooth data, the solution depends smoothly
on the parameters and has the spatial and forward-time derivatives used
below, including at $`t=0`$.*

</div>

<div class="proof">

*Proof.* On a small neighborhood $`Q`$ remains uniformly positive
definite and bounded. The principal linearized coefficient is
$`Q^{-2}`$, or $`bQ^{-2}+c(\det Q)^{-1}Q^{-1}`$; it is uniformly
positive for fixed $`b,c\ge0`$, $`b+c>0`$. The nonlinear operator is
smooth there. Apply the closed-manifold local existence theorem and
linear Schauder isomorphism of . On a fixed short cylinder, the map
$`s\mapsto(s_t-F(s),s(0))`$ has invertible derivative in parabolic
Hölder spaces. The Banach implicit-function theorem therefore supplies
the same interval for nearby data and smooth parameter dependence.
Spatial bootstrap gives the stated derivatives for smooth data;
$`C^{6,\alpha}`$ control is more than needed for endpoint $`C^2`$
continuity. This is entirely a forward-time argument. ◻

</div>

The lemma applies near $`s_0`$ to the $`\mu`$ family and near the fixed
positive-$`\mu`$ datum to the asymmetric perturbations in
Corollary <a href="#cor:robust" data-reference-type="ref"
data-reference="cor:robust">6</a>.

At $`p=(0,0,1)`$, use the chart $`(x,y,\sqrt{1-x^2-y^2})`$. At
$`t=\mu=0`$, the exact jets are
``` math
\begin{equation}
\label{eq:jets}
 \begin{gathered}
 s=1,\quad s_x=s_y=s_{xx}=s_{xy}=0,\
 s_{yy}=\varepsilon,\qquad s_{xxx}=\varepsilon,
 \qquad s_{xyy}=-4\varepsilon.
 \end{gathered}
\end{equation}
```
The Christoffel symbols vanish at this chart origin. Because
$`\nabla s=0`$, the relevant third partial derivatives equal the
covariant third derivatives there. Thus
$`Q_s=\operatorname{diag}(1,1+\varepsilon)`$ at the pole, and
differentiating <a href="#eq:mcf" data-reference-type="eqref"
data-reference="eq:mcf">[eq:mcf]</a> gives
``` math
\begin{equation}
\label{eq:sxt}
 s_{xt}=\mathop{\mathrm{tr}}(Q_s^{-1}(\partial_xQ_s)Q_s^{-1})
 =\varepsilon\left(1-\frac4{(1+\varepsilon)^2}\right)
 =-\frac{29799}{1020100}<0.
\end{equation}
```
This has the opposite sign from the positive cubic derivative in
<a href="#eq:jets" data-reference-type="eqref"
data-reference="eq:jets">[eq:jets]</a>, the orientation for a birth.

To make the event occur at positive time from nondegenerate initial
data, let $`s(x,y,t;\mu)`$ be the forward solution and put
``` math
G(x,t,\mu)=s_x(x,0,t;\mu).
```
Reflection symmetry gives $`s_y(x,0,t;\mu)=0`$. At
$`(x,t,\mu)=(0,0,0)`$,
``` math
\begin{gathered}
 G=G_x=0,\quad G_{xx}=\varepsilon,\quad
 G_\mu=\varepsilon,\quad G_{x\mu}=0,\\
 G_t=-\varepsilon k,\qquad
 k=\frac4{(1+\varepsilon)^2}-1=\frac{29799}{10201}>0.
 \end{gathered}
```
The derivative of $`(G,G_x)`$ with respect to $`(\mu,x)`$ is
$`\operatorname{diag}(\varepsilon,\varepsilon)`$, hence invertible. The
parameter-dependent implicit-function theorem, applied for forward
$`t\ge0`$, supplies the fold curve
``` math
\mu_*(t)=kt+O(t^2),\qquad x_*(t)=O(t).
```
One may apply the theorem at each forward time in a common local
neighborhood; no negative-time solution is required. Since
$`\mu_*'(0)=k>0`$, the curve can be inverted:
``` math
t_*(\mu)=\mu/k+O(\mu^2)>0\qquad(0<\mu\text{ sufficiently small}).
```

The transverse derivative $`s_{yy}`$ remains positive. By the
implicit-function theorem the only nearby solution of $`s_y=0`$ is
$`y=0`$. The function $`G`$ has positive second $`x`$-derivative and
negative $`t`$-derivative at its fold. Its local minimum crosses zero
downwards: there are no local critical points immediately before the
fold and two immediately afterwards, one minimum and one saddle. The
same is true at the antipode by central symmetry. At $`t=0`$ and small
positive $`\mu`$, the minimum of $`G`$ is $`\varepsilon\mu+O(\mu^2)>0`$,
so the initial body has no critical point in either pole neighborhood.
Section <a href="#sec:global" data-reference-type="ref"
data-reference="sec:global">4</a> proves that exactly 22 other, Morse,
points persist and that no other births interfere on the common short
interval. This completes the fold part of
Theorem <a href="#thm:main" data-reference-type="ref"
data-reference="thm:main">1</a>.

# Exact enumeration of every initial critical point

The critical points of $`s_0`$ are those of $`f_0`$. Parameterize away
from $`y=\pm1`$ by
``` math
y=r,\qquad x=\sqrt{1-r^2}\sin\theta,\qquad
 z=\sqrt{1-r^2}\cos\theta.
```
Let $`q=r^2`$, $`t=\tan\theta`$, and
``` math
A(t)=\frac{t^3}{6(1+t^2)^2},\qquad B(t)=\frac{t}{1+t^2}.
```
Then
``` math
\begin{equation}
\label{eq:reduced}
 f_0=F(t,q)=A+q(1/2-2A-2B)+q^2(A+2B).
\end{equation}
```
We handle the coordinate exceptions explicitly.

On $`y=0`$,
``` math
\frac{d}{d\theta}\left(\frac{\sin^3\theta\cos\theta}{6}\right)
 =\frac{\sin^2\theta}{6}(3\cos^2\theta-\sin^2\theta).
```
There are the two degenerate points $`(0,0,\pm1)`$ and four Morse points
with $`\tan\theta=\pm\sqrt3`$. At $`t=\pm\sqrt3`$, the transverse second
derivative is $`1\mp9\sqrt3/8`$, and the angular second derivative has
the same sign. These four points comprise two minima and two maxima.

At $`(0,\pm1,0)`$, the Hessian in local $`(x,z)`$ coordinates is
``` math
\begin{pmatrix}-1&-2\\-2&-1\end{pmatrix},
```
so these are two saddles. At $`z=0`$ with $`0<|y|<1`$, the derivative
$`F_q`$ is $`1/2`$; there are no missing critical points on that chart
boundary.

For the remaining points, $`0<q<1`$ and $`t`$ is finite. The equation
$`F_t=0`$ yields
``` math
\begin{equation}
\label{eq:qstar}
 q=q_*(t)=\frac{t^2(t^2-3)}{D(t)},\qquad D(t)=13t^4-3t^2-12.
\end{equation}
```
If $`D(t)=0`$, the numerator that must vanish in $`F_t`$ cannot vanish,
so no solution is lost by division. Substituting
<a href="#eq:qstar" data-reference-type="eqref"
data-reference="eq:qstar">[eq:qstar]</a> into $`F_q=0`$ gives
``` math
\begin{equation}
\label{eq:quartic}
 p(t)=13t^4-52t^3-3t^2+48t-12=0,
 \qquad F_q(t,q_*(t))=\frac{p(t)}{2D(t)}.
\end{equation}
```
The discriminant is $`25315198272`$, and $`p`$ is relatively prime to
$`D`$. Exact Sturm counts isolate its four simple real roots as follows;
each root corresponds to four sphere points, from the two signs of $`y`$
and the two antipodal choices of $`(x,z)`$.

<div class="center">

| Rational root interval | Roots | Sphere points | Type    |
|:-----------------------|:------|:--------------|:--------|
| $`(-99/100,-98/100)`$  | 1     | 4             | Maximum |
| $`(27/100,28/100)`$    | 1     | 4             | Saddle  |
| $`(88/100,89/100)`$    | 1     | 4             | Minimum |
| $`(382/100,383/100)`$  | 1     | 4             | Saddle  |

</div>

This table concerns the limiting initial surface at $`\mu=0`$, not a
numerically sampled positive-time trajectory. In each interval
$`0<q_*(t)<1`$. The exact Hessian determinant in $`(t,r)`$ coordinates
at a critical point is
``` math
\begin{equation}
\label{eq:hessdet}
 -\frac{16t^2(t-1)(t+1)(t^2-3)
 (169t^6-429t^4+504t^2-144)}
 {(1+t^2)^2(13t^4-3t^2-12)^3}.
\end{equation}
```
The transverse Hessian sign is the sign of
$`F_{qq}=t(13t^2+12)/(3(1+t^2)^2)`$, hence the sign of $`t`$. Sturm
counts certify that no numerator or denominator affecting the
classification vanishes in any listed interval. Evaluation at a rational
midpoint then certifies all the displayed signs.

Adding the exceptional charts gives exactly 6 minima, 6 maxima and 10
saddles, together with the two degenerate pole points. The Morse counts
satisfy $`6+6-10=2`$, as a consistency check. Compactness bounds the
gradient away from zero outside fixed small neighborhoods of these 24
points. The 22 Morse points persist under sufficiently small changes of
$`\mu`$ and sufficiently short forward evolution. The two remaining
neighborhoods are completely described by
Section <a href="#sec:fold" data-reference-type="ref"
data-reference="sec:fold">3</a>. The counts before and after the births
are therefore exactly 22 and 26, proving
Theorem <a href="#thm:main" data-reference-type="ref"
data-reference="thm:main">1</a>.

# Extensions to abrasion speeds and nonsymmetric ensembles

<div id="thm:bloore" class="theorem">

**Theorem 5** (Nonnegative Bloore-type combinations). *Let
``` math
v=a+b(\kappa_1+\kappa_2)+c\kappa_1\kappa_2,
 \qquad a,b,c\ge0,\quad b+c>0,
```
be the inward normal speed. The family
<a href="#eq:support" data-reference-type="eqref"
data-reference="eq:support">[eq:support]</a>, for all sufficiently small
positive $`\mu`$, again has a centroidal equilibrium increase from 22 to
26 at positive time. The allowed $`\mu`$ interval may depend on
$`a,b,c`$.*

</div>

<div class="proof">

*Proof.* The support equation is
``` math
s_t=-a-b\mathop{\mathrm{tr}}(Q_s^{-1})-c(\det Q_s)^{-1}.
```
At the pole the null-direction gradient derivative is
``` math
\begin{equation}
\label{eq:bloorejet}
 s_{xt}=\varepsilon\left[
 b\left(1-\frac4{(1+\varepsilon)^2}\right)
 +c\left(\frac1{1+\varepsilon}-\frac4{(1+\varepsilon)^2}\right)
 \right]<0.
\end{equation}
```
Both brackets are negative; the Gaussian contribution, including
$`\varepsilon`$, is $`-299/10201`$. The constant speed has zero spatial
derivative. The equation is strictly parabolic near the initial data,
because $`v_{\kappa_i}=b+c\kappa_j>0`$. Equivalently, the derivative of
its support operator in the curvature-radius matrix is a positive
combination of $`Q^{-2}`$ and $`(\det Q)^{-1}Q^{-1}`$. Local existence,
uniqueness and parameter dependence follow from the same uniformly
parabolic theory. Every remaining part of the preceding argument applies
unchanged, with $`k=-s_{xt}/\varepsilon>0`$. ◻

</div>

This includes mean-curvature and Gaussian-curvature flow and the
spherical-abrader speed $`(1+R\kappa_1)(1+R\kappa_2)`$ with $`R>0`$,
discussed in . It does not include pure constant-speed flow $`b=c=0`$,
for which the strict-parabolic and local-birth arguments used here do
not apply.

<div id="cor:robust" class="corollary">

**Corollary 6** (Open-set and ensemble robustness). *For each fixed flow
in Theorem <a href="#thm:bloore" data-reference-type="ref"
data-reference="thm:bloore">5</a>, there are times $`0<\tau_-<\tau_+`$
and an open set of smooth strictly convex initial bodies, including
asymmetric bodies, whose centroidal equilibrium counts satisfy
``` math
N(\tau_-)=22,\qquad N(\tau_+)=26.
```
Any probability measure supported on this open set has an expected-count
increase between these times. A nondegenerate example is the uniform law
on a sufficiently small positive parameter interval in
<a href="#eq:support" data-reference-type="eqref"
data-reference="eq:support">[eq:support]</a>.*

</div>

<div class="proof">

*Proof.* Fix a sufficiently small $`\mu>0`$, and choose
$`\tau_-,\tau_+`$ strictly before and after its birth time, while all
equilibria at the two endpoints are Morse. Solutions depend continuously
on their smooth initial support functions, on a common time interval and
in the $`C^2`$ norm at these endpoints. The homogeneous centroid also
depends continuously on the body; recentering replaces $`s(u)`$ by
$`s(u)-G\cdot u`$. Thus the centered support functions at the two
endpoints remain $`C^2`$-close for sufficiently small perturbations of
the initial body. Morse critical-point counts on the compact sphere are
stable under such perturbations: their Hessians stay invertible locally
and the gradient stays bounded away from zero elsewhere. The counts are
therefore fixed at 22 and 26 on an open neighborhood in a sufficiently
high smooth norm. This neighborhood contains asymmetric bodies, for
which the centroid need not stay fixed. Integrating the two constant
endpoint counts against any supported probability measure proves the
expectation claim. Continuity of the parameter family gives a
nonzero-length interval of positive $`\mu`$ values inside this
neighborhood. ◻

</div>

This disproves a *distribution-free* expectation claim. It is not a
claim that the ensemble in
Corollary <a href="#cor:robust" data-reference-type="ref"
data-reference="cor:robust">6</a> satisfies the random-jet moment
assumptions of , or that it represents naturally sampled rocks.

# An exact obstruction to the stochastic moment argument

In the notation of , put
``` math
A=\bar r_{yyy},\quad B=\bar r_{xxy},\quad
 \alpha=v_\kappa>0,\quad\beta=v_\lambda>0.
```
The annihilation indicator and jump size are
``` math
\begin{equation}
\label{eq:sign}
 \Omega=\mathop{\mathrm{sgn}}(\alpha A^2+\beta AB),\qquad \Delta N=-2\Omega.
\end{equation}
```
Assumption 2 is $`\mathbb EA=\mathbb EB=\mathop{\mathrm{Cov}}(A,B)=0`$.
This gives a positive expectation for the expression inside the sign,
provided $`A`$ has nonzero variance, but does not determine the expected
sign.

<div id="prop:law" class="proposition">

**Proposition 7** (Four-outcome counterexample). *Even when
$`\alpha=\beta=1`$, both marginal laws are symmetric, all moments are
finite, and the three moment conditions in Assumption 2 hold, one can
have
``` math
\mathbb E(A^2+AB)=1>0,\qquad \mathbb E\Omega=-\frac45,
 \qquad\mathbb E\Delta N=\frac85>0.
```*

</div>

<div class="proof">

*Proof.* Use this probability law:

<div class="center">

| Probability |  $`A`$ |   $`B`$ | $`A^2+AB`$ |
|------------:|-------:|--------:|-----------:|
|    $`9/20`$ |      1 |  $`-2`$ |     $`-1`$ |
|    $`9/20`$ | $`-1`$ |       2 |     $`-1`$ |
|    $`1/20`$ |      1 |      18 |         19 |
|    $`1/20`$ | $`-1`$ | $`-18`$ |         19 |

</div>

The paired outcomes give $`\mathbb EA=\mathbb EB=0`$. Also
``` math
\mathbb EAB=\frac9{10}(-2)+\frac1{10}(18)=0,
 \quad \mathbb EA^2=1,\quad \mathbb EB^2=36.
```
Yet the inside expression is negative with probability $`9/10`$,
positive with probability $`1/10`$, and never zero. Thus
$`\mathbb E\Omega=1/10-9/10=-4/5`$, and
<a href="#eq:sign" data-reference-type="eqref"
data-reference="eq:sign">[eq:sign]</a> gives the positive mean jump. ◻

</div>

The step from equation (50) to (51) in is therefore false under its
stated moment hypothesis, and the resulting embedded jump-chain drift is
not determined by those moments. The example also survives the addition
of an independent uniform noise $`\eta\in[-d,d]`$ for any $`0<d<1`$:
neither of the values $`-1`$ and 19 changes sign. Thus adding small
independent centered noise to this moment model does not repair the
inference. This observation does not identify $`AB`$ with the
alternative determinant-sampling variable in Assumption 2-A.

<div id="prop:sharp" class="proposition">

**Proposition 8** (The sign can vary across its full range). *Under the
same zero-mean and zero-covariance constraints, with $`\mathbb EA^2=1`$,
$`\mathbb E\mathop{\mathrm{sgn}}(A^2+AB)`$ can take every value in
$`(-1,1)`$.*

</div>

<div class="proof">

*Proof.* Let $`A`$ be a symmetric Rademacher variable, independent of
$`R`$. For any $`q\in(0,1)`$, take
``` math
\mathbb P(R=-2)=q,\qquad
 \mathbb P\left(R=\frac{2q}{1-q}\right)=1-q,
 \qquad B=RA.
```
Then $`\mathbb ER=0`$, hence $`\mathbb EA=\mathbb EB=\mathbb EAB=0`$,
while $`A^2+AB=1+R`$. Its expected sign is $`1-2q`$ and its expectation
is 1. Every member of this family has finite variance; no common
variance bound is asserted as $`q\to1`$. ◻

</div>

## A correct probability criterion and sufficient hypotheses

<div id="thm:criterion" class="theorem">

**Theorem 9** (Exact drift criterion). *Suppose $`A\ne0`$ almost surely
and $`\mathbb P(\alpha A^2+\beta AB=0)=0`$, with $`\alpha,\beta>0`$.
Then
``` math
\begin{equation}
\label{eq:criterion}
 \mathbb E\Delta N=-2+4\mathbb P\{A(\alpha A+\beta B)<0\}.
\end{equation}
```
Consequently nonpositive mean jump is equivalent to the probability on
the right being at most $`1/2`$. A sufficient condition is symmetry of
the conditional law of $`B`$ given $`A`$, around zero. Independence of
$`A,B`$, together with symmetry of $`B`$, is a stronger sufficient
condition.*

</div>

<div class="proof">

*Proof.* There are only the two signs, so
$`\mathbb E\Omega=1-2\mathbb P(\Omega=-1)`$, proving
<a href="#eq:criterion" data-reference-type="eqref"
data-reference="eq:criterion">[eq:criterion]</a>. Conditional on
$`A=a>0`$, a negative sign requires $`B<-\alpha a/\beta`$. Conditional
on $`A=a<0`$, it requires $`B>\alpha|a|/\beta`$. Under conditional
symmetry each probability is at most $`1/2`$. Integrating proves the
claim. Strictly negative drift needs additional conditional mass inside
the corresponding threshold intervals; symmetry alone can yield zero
drift. ◻

</div>

For example, independent symmetric variables $`A=\pm1`$ and $`B=\pm2`$,
with $`\alpha=\beta=1`$, have zero mean drift rather than the 75%
annihilation probability quoted under symmetry in equation (52) of .
Identical distribution is a useful additional sufficient hypothesis: if
$`A,B`$ are independent, identically distributed, continuous and
symmetric, the event $`AB<0`$ has probability $`1/2`$, independently of
their magnitudes, and exchangeability gives $`\mathbb P(|B|>|A|)=1/2`$.
Thus the creation probability is $`1/4`$, and the annihilation
probability is $`3/4`$, when $`\alpha=\beta`$.

More generally, independent centered Gaussians with positive standard
deviations $`\sigma_A,\sigma_B`$ give the explicit formula
``` math
\mathbb E\Omega=\frac2\pi\arctan\left(\frac{\alpha\sigma_A}{\beta\sigma_B}\right),
 \qquad
 \mathbb E\Delta N=-\frac4\pi\arctan\left(\frac{\alpha\sigma_A}{\beta\sigma_B}\right)<0.
```
Indeed, after standardization the joint normal vector has uniform polar
angle, so its coordinate ratio is standard Cauchy. The sign is negative
precisely when $`B/A<-\alpha/\beta`$. Integrating the Cauchy density
gives the formula. This also shows why the individual variances can
matter, despite their absence from the moment condition.

A continuous-time expected-count theorem additionally needs conditional
drift conditions at each state and a well-defined nonexplosive
event-rate/holding-time model.
Equation <a href="#eq:criterion" data-reference-type="eqref"
data-reference="eq:criterion">[eq:criterion]</a> resolves the local
embedded-jump question; it does not prescribe such a model or an
empirical rock ensemble.

# Verification, dependencies and scope

The script uses exact SymPy algebra and rational probability arithmetic.
It verifies the support-function symmetry, the displayed jets, both
curvature-flow signs, the rational convexity majorant, the
critical-point reduction, Sturm root counts, all Hessian
classifications, the final 22/26 counts and the four-outcome moments.
The Gaussian and conditional-symmetry statements above are proved
directly, not by simulation.

The continuum conclusion also uses smooth short-time existence,
uniqueness and parameter dependence for uniformly parabolic curvature
flows, and the implicit-function and Morse-persistence arguments given
here. These analytic steps are not replaced by finite sampling and are
not formalized in a proof assistant. The supplied verification report is
not an independent human referee report.

The resolved claims are: deterministic centroidal monotonicity is false
even for a smooth strictly convex centrally symmetric body under
mean-curvature flow; the failure extends to the stated Bloore-type
speeds and an open set of asymmetric bodies; a distribution-free
expected-count version is false; and the stated moment assumptions do
not imply the published drift sign. A particular fully specified
stochastic abrasion ensemble may still have decreasing expected counts
under stronger assumptions. No assertion about observed frequencies in
natural rocks follows from these mathematical counterexamples.

<div class="thebibliography">

9 Damon, J. (1995). Local Morse theory for solutions to the heat
equation and Gaussian blurring. *Journal of Differential Equations,
115*(2), 368–401. <https://doi.org/10.1006/jdeq.1995.1019>.

Huang, H. (2026). The Cauchy problem for fully nonlinear parabolic
systems on manifolds. arXiv:1506.05030v8, 25 August 2026; first posted
2015. <https://arxiv.org/abs/1506.05030v8>.

Domokos, G. (2015). Monotonicity of spatial critical points evolving
under curvature-driven flows. *Journal of Nonlinear Science, 25*,
247–275. Published online 2014.
<https://doi.org/10.1007/s00332-014-9228-3>. Author version, v4:
<https://arxiv.org/abs/1308.4779>.

Huisken, G. (1984). Flow by mean curvature of convex surfaces into
spheres. *Journal of Differential Geometry, 20*(1), 237–266.
<https://doi.org/10.4310/jdg/1214438998>. Related author lecture:
<https://maths.anu.edu.au/files/CMAProcVol8-Huisken_1.pdf>.

</div>
