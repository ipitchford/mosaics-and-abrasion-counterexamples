<div class="center">

Unrefereed candidate. DOI: <https://doi.org/10.5281/zenodo.23167002>

</div>

**Keywords.** Convex mosaic; harmonic degree; power diagram; Schlegel
diagram; neighborly cubical polytope; flag vector; exact certificate.

# Problem, conventions and contribution

A convex mosaic in $`\mathbb R^d`$ is a locally finite tiling by
full-dimensional compact convex polytopes with disjoint interiors. It is
*face-to-face* when the intersection of any two cells is empty or a face
of both. It is *normal* when there are positive constants $`r,R`$,
depending on the mosaic, such that every cell contains a ball of radius
$`r`$ and is contained in a ball of radius $`R`$. These constants need
not be uniform across a sequence of different mosaics.

We use the notation of : $`\overline n`$ is the mean number of cells at
a vertex, and $`\overline v`$ is the mean number of vertices of a cell.
The supplied problem bundle interchanges these two symbols; their
harmonic combination is unchanged. For a periodic mosaic, write
$`V,C,I`$ for vertex, cell and vertex–cell incidence counts per
fundamental volume, counting orbits with their incidence multiplicities.
Then
``` math
\begin{equation}
\label{eq:basic}
 \overline n=\frac I V,\qquad \overline v=\frac I C,\qquad
 \overline h=\frac{\overline n\overline v}{\overline n+\overline v}=\frac I{V+C}.
\end{equation}
```
The same formulas hold for the densities of the nonperiodic
constructions below. Bounded cell diameters and finitely many local
types make the discrepancy between cell-based and vertex-based incidence
counts a boundary term of order $`O(R^{d-1})`$ in a radius-$`R`$
observation window.

proposed $`\overline h\in(d,2^{d-1}]`$, hence $`3<\overline h\le4`$ in
dimension three. Their existence theorem supplies all values in the
proposed interval; their general three-dimensional lower estimate is
$`28/13`$. Our counterexample satisfies all the geometric hypotheses,
not merely formal incidence equations.

#### Prior-art boundary.

The underlying polytopes are not new: neighborly cubical polytopes are
due to , and the larger-complexity projected products are due to .
Moreover, explicitly describes replacing tetrahedra in a space tiling by
Schlegel diagrams, discusses high mean vertex and tile degrees, and
relates tiling questions to polytope complexity and liftability. Thus
neither the insertion device nor qualitative one-coordinate
unboundedness should be advertised as a new invention. We provide
complete count formulas, a small rational counterexample to the later
conjecture, a periodic power-diagram certificate, and an explicit
asymptotic comparison restricted to a class for which the converse
lifting is justified.

The finite counterexample is self-contained: its four-polytope is
checked directly from rational inequalities in
Appendix <a href="#sec:rational" data-reference-type="ref"
data-reference="sec:rational">9</a>. The existence of the asymptotic
family approaching 16 uses the stated published projected-product
theorem. The lower-bound corollary in
Section <a href="#sec:equivalence" data-reference-type="ref"
data-reference="sec:equivalence">7</a> uses the established
four-polytope flag inequality. These dependencies are not computational
conjectures.

<div class="center">

| Published input | Modification established here | Conclusion here |
|:---|:---|:---|
| Cubical polytopes | Rational specialization, two stackings, complete finite certificate | Explicit harmonic degree $`468/115>4`$ |
| Schlegel insertion ; lifting background | Strict periodic implantation and rational site payload | Weighted-Delaunay and Laguerre counterexamples |
| Projected products | Exact insertion costs and unchanged-boundary mixing | Approach to 16; every value in $`(3,16)`$ |
| Four-polytope complexity | Vanishing port cost in one direction; capped periodic epigraph in the other | Equality of finite limit sets in Theorem <a href="#thm:equivalence" data-reference-type="ref"
data-reference="thm:equivalence">15</a> |

</div>

The general relationship between liftings and weighted diagrams is
inherited background, not a novelty claim. The comparison theorem below
is restricted to the stated periodic regular class.

<div id="thm:main" class="theorem">

**Theorem 1** (Certified counterexample). *There is a normal, periodic,
face-to-face convex mosaic $`\mathcal M`$ of $`\mathbb R^3`$ with
``` math
(V,C,I)=(373,432,3276),\qquad
 (\overline n,\overline v)=\left(\frac{3276}{373},\frac{91}{12}\right),
 \qquad \overline h=\frac{468}{115}=4+\frac8{115}.
```
It has a rational realization. After a rational affine change of metric,
it is a periodic weighted-Delaunay subdivision. Its Laguerre dual is a
normal periodic convex mosaic with the two mean degrees exchanged and
the same harmonic degree. Thus the proposed upper bound fails even for
periodic Laguerre mosaics.*

</div>

# Tetrahedral insertion and exact incidence accounting

For a four-polytope $`P`$, let $`f_i(P)`$ count its $`i`$-faces and let
$`f_{03}(P)`$ count incident vertex–facet pairs. A facet of a
four-polytope is a three-polytope.

<div id="lem:schlegel" class="lemma">

**Lemma 2** (Schlegel template). *Let $`P\subset\mathbb R^4`$ have a
tetrahedral facet $`F`$. There is a convex face-to-face subdivision of
$`F`$ with
``` math
a=f_0(P)\text{ vertices},\quad a-4\text{ interior vertices},\quad
 b=f_3(P)-1\text{ cells},\quad j=f_{03}(P)-4\text{ incidences}.
```
Its boundary is precisely the unsubdivided boundary of $`F`$. The
subdivision has a strictly regular lifting whose boundary heights are
zero. Rational input data admit rational choices throughout.*

</div>

<div class="proof">

*Proof.* Choose a point $`z`$ just beyond $`F`$, and strictly beneath
all other facet hyperplanes. Central projection from $`z`$ to
$`\mathop{\mathrm{aff}}F`$ maps the boundary of $`P`$, with the relative
interior of $`F`$ removed, onto $`F`$. Each ray enters $`P`$ through
$`F`$ and exits on one of the other facets. Consequently the projected
facets cover $`F`$, their interiors are disjoint, and their
intersections are projected common faces. Projection is projective and
finite on each of these facets, so each image is a convex polytope of
the same combinatorial type.

Every vertex outside $`F`$ projects strictly inside $`F`$. No additional
boundary face or vertex appears. Removing the outer facet removes
exactly four vertex–facet incidences, giving the displayed counts.

For regularity, let $`h\le0`$ be the outer facet inequality and put
$`s=h(z)>0`$. For a point $`p\in P`$, set
``` math
t(p)=\frac{s}{s-h(p)},\qquad y(p)=z+t(p)(p-z).
```
The map $`p\mapsto(y(p),t(p)-1)`$, with $`y`$ coordinatized on
$`\mathop{\mathrm{aff}}F`$, is a nonsingular projective transformation
on a neighborhood of $`P`$. Its image is a convex four-polytope with top
facet $`F\times\{0\}`$. All remaining facets are lower facets: over an
interior point of $`F`$, the segment from the entrance to the exit of
the ray runs downward from height zero to the exit height. Distinct
facets give distinct supporting affine functions. This is the claimed
strictly regular lifting. Strict inequalities define open choices, and
all operations preserve rationality when the chosen viewpoint is
rational. ◻

</div>

<div id="lem:insert" class="lemma">

**Lemma 3** (Insertion counts). *Suppose a tetrahedron has a convex
face-to-face subdivision with $`a`$ vertices, exactly four on its
boundary, $`b`$ cells and $`j`$ vertex–cell incidences. Replacing every
tetrahedron in the Freudenthal triangulation of $`\mathbb R^3`$ by an
affine copy of this subdivision produces a normal periodic mosaic with
``` math
\begin{equation}
\label{eq:insert}
 V=1+6(a-4),\qquad C=6b,\qquad I=6j.
\end{equation}
```*

</div>

<div class="proof">

*Proof.* For $`z\in\mathbb Z^3`$ and a permutation $`\pi`$ of $`1,2,3`$,
use the tetrahedron with ordered vertices
``` math
z,\quad z+e_{\pi(1)},\quad z+e_{\pi(1)}+e_{\pi(2)},\quad z+(1,1,1).
```
These six tetrahedra triangulate every unit cube compatibly. Because the
template boundary is not subdivided, neighboring copies agree exactly on
every common triangle, edge and vertex. Each unit volume has one
original lattice vertex and six sets of $`a-4`$ new interior vertices.
Cells and their incidences are assigned to unique macro-tetrahedra,
proving <a href="#eq:insert" data-reference-type="eqref"
data-reference="eq:insert">[eq:insert]</a>.

There are finitely many nondegenerate cell shapes, up to translation.
The minimum of their positive inradii and the maximum of their
circumradii establish normality. Periodicity gives the required
averages. Convexity and face matching follow from the affine images of
the template and its unchanged boundary. ◻

</div>

<div id="cor:polytocount" class="corollary">

**Corollary 4**. *For a four-polytope with a tetrahedral facet, the
inserted mosaic has
``` math
\begin{equation}
\label{eq:polytocount}
 V=6f_0-23,\quad C=6(f_3-1),\quad I=6(f_{03}-4),\quad
 \overline h=\frac{f_{03}-4}{f_0+f_3-29/6}.
\end{equation}
```*

</div>

# Two stackings and the finite counterexample

Stacking beyond a facet means taking the convex hull with a new point
beyond that facet and strictly beneath every other facet. The old facet
disappears and is replaced by pyramids over its two-dimensional faces.
The existence of such a point follows by moving a sufficiently small
distance outward from a relative-interior point of the facet.

<div id="lem:port" class="lemma">

**Lemma 5** (A tetrahedral boundary from a cube). *If a four-polytope
has a cubical facet, two stackings produce a four-polytope with a
tetrahedral facet, changing $`(f_0,f_3,f_{03})`$ by $`(2,9,38)`$.*

</div>

<div class="proof">

*Proof.* Stack beyond the cube. It has six quadrilateral faces. The
removed facet has eight vertices, and the six replacement square
pyramids each have five vertices. Hence the changes are
``` math
\Delta f_0=1,\qquad \Delta f_3=6-1=5,\qquad
 \Delta f_{03}=6\cdot5-8=22.
```
Now stack beyond any new square pyramid. Its five faces are one square
and four triangles. The replacement facets are one square pyramid and
four tetrahedra, giving
``` math
\Delta f_0=1,\qquad \Delta f_3=5-1=4,\qquad
 \Delta f_{03}=5+4\cdot4-5=16.
```
A new tetrahedral facet is available, and addition gives the result. ◻

</div>

Neighborly cubical four-polytopes $`P_n`$, $`n\ge4`$, have the graph of
the $`n`$-cube and cubical facets. Their established face numbers are
``` math
\begin{equation}
\label{eq:ncp}
 f_0=2^n,\quad f_1=n2^{n-1},\quad
 f_2=3(n-2)2^{n-2},\quad f_3=(n-2)2^{n-2},\quad f_{03}=8f_3.
\end{equation}
```
For completeness, once existence and the cube graph are given, the
formulas follow from $`f_0=2^n`$, $`2f_1=n2^n`$, ridge double counting
$`f_2=3f_3`$, and Euler’s relation $`f_0-f_1+f_2-f_3=0`$. Existence is
due to . For $`n=6`$ we instead provide the full rational verification
below.

Applying Lemma <a href="#lem:port" data-reference-type="ref"
data-reference="lem:port">5</a>, followed by Schlegel projection and
insertion, gives
``` math
\begin{align}
\label{eq:nfamily}
 V_n&=6\cdot2^n-11,\nonumber\\
 C_n&=6\bigl((n-2)2^{n-2}+8\bigr),\\
 I_n&=6\bigl(8(n-2)2^{n-2}+34\bigr).\nonumber
\end{align}
```
At $`n=6`$, the complete accounting is as follows.

<div class="center">

| Object                           | Vertices | Facets/cells | Incidences |
|:---------------------------------|---------:|-------------:|-----------:|
| Cubical four-polytope            |       64 |           64 |        512 |
| After first stacking             |       65 |           69 |        534 |
| After second stacking            |       66 |           73 |        550 |
| Tetrahedral Schlegel patch       |       66 |           72 |        546 |
| Periodic mosaic, per unit volume |      373 |          432 |       3276 |

</div>

The patch has 62 interior vertices; the periodic count is therefore
$`1+6\cdot62=373`$, not $`6\cdot66`$. This boundary identification is
essential. Equation <a href="#eq:basic" data-reference-type="eqref"
data-reference="eq:basic">[eq:basic]</a> gives
``` math
\overline h=\frac{3276}{373+432}=\frac{468}{115}>4,
 \qquad \overline v=\frac{3276}{432}=\frac{91}{12}.
```
Lemmas <a href="#lem:schlegel" data-reference-type="ref"
data-reference="lem:schlegel">2</a> and
<a href="#lem:insert" data-reference-type="ref"
data-reference="lem:insert">3</a> prove the geometric assertions in
Theorem <a href="#thm:main" data-reference-type="ref"
data-reference="thm:main">1</a>. Rationality follows from
Appendix <a href="#sec:rational" data-reference-type="ref"
data-reference="sec:rational">9</a>. The regular and Laguerre assertions
are proved next. The family
<a href="#eq:nfamily" data-reference-type="eqref"
data-reference="eq:nfamily">[eq:nfamily]</a> also gives
``` math
\overline h_n\longrightarrow8,\qquad \overline n_n\sim2n,\qquad \overline v_n\longrightarrow8.
```

# A periodic weighted-Delaunay and Laguerre realization

A weighted site $`(p,w)`$ has power distance $`\|x-p\|^2-w`$. Its
Laguerre cell consists of points for which this power distance is
minimal among the sites. The dual weighted-Delaunay complex is obtained
from lower faces of the lifted points $`(p,\|p\|^2-w)`$. Nonsimplicial
lower faces are retained; no generic perturbation or arbitrary
triangulation is applied.

<div id="lem:regular" class="lemma">

**Lemma 6** (Regular implantation). *A finite strictly regular
tetrahedral subdivision with no boundary subdivision can be implanted
periodically in the Freudenthal triangulation so that the resulting
mosaic is a weighted-Delaunay subdivision in a Euclidean metric.
Rational template coordinates and heights give rational periodic site
coordinates and weights after a rational linear transformation.*

</div>

<div class="proof">

*Proof.* Let $`J`$ be the $`3\times3`$ all-ones matrix and choose
``` math
Q=I-\frac5{16}J,\qquad A=I-\frac14J,\qquad A^{\mathsf T}A=Q.
```
The eigenvalues of $`Q`$ are $`1,1,1/16`$, so $`q(x)=x^{\mathsf T}Qx`$
is positive definite. Interpolate its lattice values affinely on the
Freudenthal tetrahedra, obtaining $`L`$.

We verify that $`L`$ is convex and has a strict bend at each macro-face.
Inside a unit cube, its simplices correspond to descending orders of the
fractional coordinates. If two adjacent coordinates exchange order, the
convexity gap is $`-2Q_{ij}>0`$. Across a coordinate-integer plane, the
entering and leaving simplices have gradient jump
$`2\sum_jQ_{ij}=1/8>0`$ in the normal coordinate. These are all
macro-face types. Thus every bend is strict. The interpolation also
satisfies
``` math
\begin{equation}
\label{eq:quasiper}
 L(x+z)=L(x)+2(Qz)\cdot x+q(z),\qquad z\in\mathbb Z^3.
\end{equation}
```

Let $`g`$ be the convex piecewise-affine template lifting, normalized to
zero on the tetrahedron boundary. Transfer the same $`g`$ affinely to
each macro-tetrahedron, and call the resulting continuous function
$`G`$. It is convex inside each macro-tetrahedron, although it can have
concave bends on macro-faces. Only finitely many pairs of adjacent
template types occur. Consequently for all sufficiently small
$`\delta>0`$,
``` math
H=L+\delta G
```
is convex on the whole space and still strictly bent at every
macro-face. Within a macro-tetrahedron its maximal affine pieces are
exactly the template cells. Local convexity across all faces implies
global convexity by restricting to a generic line segment and observing
nondecreasing successive slopes, then taking limits for nongeneric
segments.

The inserted vertex set has finitely many representatives $`x_i`$ modulo
$`\mathbb Z^3`$. Use Euclidean sites $`p_i=Ax_i`$ and weights
``` math
w_i=q(x_i)-H(x_i).
```
Because $`G`$ is periodic and
<a href="#eq:quasiper" data-reference-type="eqref"
data-reference="eq:quasiper">[eq:quasiper]</a> holds, the weight is
unchanged when $`x_i`$ is translated by $`\mathbb Z^3`$. All lifted site
heights are $`H(x_i)`$; convexity says their lower faces are precisely
the constructed mosaic. A rational $`\delta`$ can be chosen using
finitely many strict rational inequalities. ◻

</div>

<div id="lem:dual" class="lemma">

**Lemma 7** (Duality and normality). *For the periodic weighted-Delaunay
mosaics above, the Laguerre dual is a normal periodic face-to-face
convex mosaic. Its density triple is $`(C,V,I)`$, and its mean degrees
are $`(\overline v,\overline n)`$.*

</div>

<div class="proof">

*Proof.* An exposed lower facet corresponds to a Laguerre vertex; an
exposed lower vertex corresponds to a full-dimensional Laguerre cell.
The lower hull therefore gives an incidence-reversing duality between
the two polyhedral complexes, including nonsimplicial faces. Strict
convexity across every cell face ensures that no listed facet is
artificially split into coplanar cells.

There are finitely many site and weight types per period, the sites are
relatively dense, and the weights are bounded. Comparing a distant site
with a uniformly nearby site shows that every nonempty power cell is
bounded, with a uniform diameter bound. All active sites correspond to
full-dimensional power cells. There are finitely many such cells up to
lattice translation, so their positive inradii have a positive minimum.
Power cells are convex intersections of halfspaces and fit face-to-face.
Dual incidences have bounded spatial displacement, hence agree in
density, giving the count exchange. ◻

</div>

#### Exact weighted-site certificate.

For the 66-vertex patch the script obtains
``` math
\delta=\frac1{256}.
```
It checks all 24 directed macro-face incidences adjacent to the six
tetrahedra in a unit cube. Every exact convexity gap is positive; their
minimum in the chosen opposite-corner normalization is
``` math
\frac{8426635718028359287}{255182159259348442040}>0.
```
The resulting file `weighted_sites_certificate.json` lists 373 rational
site representatives, their rational weights, the rational lattice
matrix $`A`$, and all 432 dual-Delaunay cell orbits. It defines a
periodic power diagram without needing an infinite search. The Laguerre
mosaic has $`(V,C,I)=(432,373,3276)`$. This completes
Theorem <a href="#thm:main" data-reference-type="ref"
data-reference="thm:main">1</a>.

# The attainable mean-degree set is unbounded

Let $`S_d`$ denote attainable $`(\overline n,\overline v)`$ pairs in
normal face-to-face convex $`d`$-mosaics with existing means.

<div id="thm:degrees" class="theorem">

**Theorem 8**. *For every $`d\ge3`$, $`S_d`$ is unbounded in each
coordinate separately. In dimension three there are periodic
weighted-Delaunay mosaics with $`\overline v=4`$ and
$`\overline n\to\infty`$, and periodic Laguerre mosaics with
$`\overline n=4`$ and $`\overline v\to\infty`$.*

</div>

<div class="proof">

*Proof.* Take the cyclic four-polytope $`C_4(m)`$, $`m\ge5`$, the convex
hull of $`(t,t^2,t^3,t^4)`$ at $`m`$ distinct real values of $`t`$. It
is simplicial and two-neighborly. One elementary proof of the edge
property is to use the nonnegative quartic $`(t-a)^2(t-b)^2`$, which
exposes any two chosen vertices. No five vertices are coplanar, by the
Vandermonde determinant, so every facet is a tetrahedron. Thus
$`f_1=\binom m2`$, and ridge double counting and Euler give
``` math
a=m,\qquad b=f_3=\binom m2-m=\frac{m(m-3)}2,\qquad f_{03}=4b.
```
Schlegel projection through any facet and insertion yield
``` math
V=6m-23,\qquad C=6(b-1),\qquad I=24(b-1).
```
Consequently
``` math
\begin{equation}
\label{eq:cyclicmeans}
 \overline v=4,\qquad \overline n=\frac{24(b-1)}{6m-23}\sim2m.
\end{equation}
```
Lemmas <a href="#lem:regular" data-reference-type="ref"
data-reference="lem:regular">6</a> and
<a href="#lem:dual" data-reference-type="ref"
data-reference="lem:dual">7</a> produce the weighted-Delaunay
realization and its Laguerre dual, proving both three-dimensional
statements.

For $`d=3+k`$, take the Cartesian product with the unit-interval tiling
in $`k`$ additional coordinates. A product cell has $`2^k`$ times as
many vertices, and a product vertex meets $`2^k`$ times as many cells.
Normality, face matching and existence of the means are preserved. Hence
both degrees, and the harmonic degree, are multiplied by $`2^k`$. ◻

</div>

This is a direct quantitative treatment of the boundedness question in
the supplied bundle. The qualitative phenomenon is already discussed in
; we do not claim priority for unboundedness itself. The preceding proof
also shows exactly why an unbounded coordinate does not force unbounded
harmonic degree: in
<a href="#eq:cyclicmeans" data-reference-type="eqref"
data-reference="eq:cyclicmeans">[eq:cyclicmeans]</a>,
$`\overline h\to4`$.

<div id="prop:planar" class="proposition">

**Proposition 9** (The planar comparison). *The full planar set is
``` math
S_2=\left\{(n,v):3\le n,v\le6,\quad \frac1n+\frac1v=\frac12\right\}.
```*

</div>

<div class="proof">

*Proof.* Euler’s relation in large windows, together with edge–cell and
edge–vertex incidence counting, gives $`\overline h=2`$. Every node and
every polygon has degree at least three, so the displayed bounds follow.

Conversely, start from the regular hexagonal tiling. In a proportion
$`p\in[0,1]`$ of its hexagons, insert the center and join it to all six
vertices, leaving all hexagon boundaries unchanged. Per original hexagon
the densities are
``` math
V=2+p,\qquad C=1+5p,\qquad I=6+12p.
```
As $`p`$ varies, $`I/V`$ increases continuously from 3 to 6 and the
required curve is traced exactly. Rational proportions can be periodic.
For any real proportion use the balanced column sequence
$`a_j=\lfloor(j+1)p\rfloor-\lfloor jp\rfloor`$. Its bounded interval
discrepancy gives the same densities in expanding disks, by summation by
parts. There are only the original hexagons and the six congruent
triangular cell types, so the mosaic is normal. ◻

</div>

# Harmonic degrees approaching 16 and interval filling

The following published input is enough; no numerical search for
high-incidence cells is required.

<div id="prop:product" class="proposition">

**Proposition 10** (Projected-product input, ). *For even $`m\ge4`$ and
integers $`r\ge3`$, there is a convex four-polytope $`P_{r,m}`$ with
``` math
\begin{equation}
\label{eq:productcounts}
 a=m^r,\quad b=\frac{r-2}{4}m^r+r m^{r-1},\quad
 j=4(r-1)m^r.
\end{equation}
```
Its facets consist of $`(r-2)m^r/4`$ combinatorial cubes and
$`r m^{r-1}`$ prisms over $`m`$-gons.*

</div>

The stated $`b,j`$ can be checked independently from the facet types:
each cube has eight vertices and each prism has $`2m`$, so
$`j=8((r-2)m^r/4)+2m(rm^{r-1})`$. The geometric existence is the
nontrivial published input. The facet count is the sum of the cube and
prism counts; the vertex–facet incidence count weights these by eight
and $`2m`$, respectively. No other flag-vector component is used here.

<div id="thm:16" class="theorem">

**Theorem 11**. *There are periodic normal weighted-Delaunay mosaics,
and their Laguerre duals, with harmonic degrees tending to 16. Moreover
every $`h\in(3,16)`$ is attained by a normal face-to-face convex mosaic.
Every rational $`h\in(3,16)`$ is attained periodically.*

</div>

<div class="proof">

*Proof.* There is a cube facet in
Proposition <a href="#prop:product" data-reference-type="ref"
data-reference="prop:product">10</a>. Apply the two-stack construction
and insert its tetrahedral Schlegel diagram. The resulting harmonic
degree is
``` math
\begin{equation}
\label{eq:hproduct}
 h_{r,m}=\frac{j+34}{a+b+37/6}
 =\frac{4(r-1)m^r+34}{m^r+(r-2)m^r/4+r m^{r-1}+37/6}.
\end{equation}
```
The additive constants are negligible, and
``` math
\frac{j}{a+b}=\frac{16(r-1)}{r+2+4r/m}\longrightarrow16
 \quad\text{as }r,m\longrightarrow\infty.
```
Regular implantation and duality apply exactly as before.

For low harmonic degrees, begin with the Freudenthal triangulation and
perform $`k`$ rounds in which every tetrahedron is subdivided into four
by joining its center to its facets. Each round leaves the outer
boundary of every original tetrahedron unchanged. Direct induction gives
``` math
C_k=6\cdot4^k,\qquad V_k=2\cdot4^k-1,\qquad I_k=24\cdot4^k,
 \qquad h_k=\frac{24\cdot4^k}{8\cdot4^k-1}\downarrow3.
```
Fix $`h\in(3,16)`$. Choose a low template with harmonic degree below
$`h`$, and a high template from
<a href="#eq:hproduct" data-reference-type="eqref"
data-reference="eq:hproduct">[eq:hproduct]</a> above $`h`$. They have
the same unsubdivided tetrahedral boundary. Place the high template in a
proportion $`p`$ of macro-tetrahedra and the low template in the rest.
Each of $`V,C,I`$ is affine in $`p`$, with the original lattice-vertex
contribution included once. Therefore $`I/(V+C)`$ is a continuous
fractional-linear function connecting the two endpoint values; its
derivative has a fixed nonzero sign. It takes the value $`h`$ for a
unique $`p\in(0,1)`$.

A periodic selection realizes every rational $`p`$. All endpoint
densities are rational, so solving the fractional-linear equation for a
rational $`h`$ gives rational $`p`$. For irrational $`p`$, assign the
same selection to all six tetrahedra of cube-column $`z_1=j`$, using
$`\lfloor(j+1)p\rfloor-\lfloor jp\rfloor`$. Interval discrepancy is
bounded by one. Summation by parts against the cross-sectional counts of
a large ball gives an $`O(R^2)`$ density error, while the total counts
are of order $`R^3`$. Finitely many cell types ensure normality. Thus
every claimed mean exists and every claimed value is attained. ◻

</div>

<div class="remark">

*Remark 12*. The interval theorem does not say that 16 is the maximum,
or that 3 cannot be attained in the full convex class. The endpoints in
the proof are limits. Periodic mosaics necessarily have rational mean
degrees, so irrational harmonic degrees require nonperiodic
constructions. The examples obtained by taking products in
Theorem <a href="#thm:degrees" data-reference-type="ref"
data-reference="thm:degrees">8</a> also contradict the upper endpoint
$`2^{d-1}`$ of the proposed band in every $`d\ge3`$.

</div>

# Asymptotic flag complexity and the regular-class frontier

Write
``` math
\rho(P)=\frac{f_{03}(P)}{f_0(P)+f_3(P)}.
```
This differs from the normalized complexity $`(f_{03}-20)/(f_0+f_3-10)`$
of , but has the same finite limits along sequences with
$`f_0+f_3\to\infty`$. Let $`\mathcal L_4`$ be the set of finite such
limits. Let $`\mathcal H_{\mathrm{pow}}`$ be the harmonic degrees of
normal periodic weighted-Delaunay mosaics in $`\mathbb R^3`$ arising
from finitely many weighted sites per period; the same set is obtained
from their Laguerre duals.

<div id="lem:generalport" class="lemma">

**Lemma 13** (General two-stack cost). *Let $`P`$ have counts
$`(a,b,j)=(f_0,f_3,f_{03})`$. Choose a facet $`G`$ with $`v`$ vertices
and $`f`$ polygonal faces, and a $`k`$-gonal face of $`G`$. Stack beyond
$`G`$, then beyond the new pyramid on this $`k`$-gon. The resulting
four-polytope has a tetrahedral facet and counts
``` math
a'=a+2,\qquad b'=b+f+k-1,\qquad
 j'=j+v+3f+4k-4.
```
The inserted mosaic has
``` math
\begin{equation}
\label{eq:generalport}
 h=\frac{j+v+3f+4k-8}{a+b+f+k-23/6}.
\end{equation}
```*

</div>

<div class="proof">

*Proof.* If $`G`$ has $`e`$ edges, its face sizes sum to $`2e`$. The
first stacking changes the incidence count by $`2e+f-v`$. Euler’s
relation $`v-e+f=2`$ rewrites this as $`v+3f-4`$. A pyramid on a
$`k`$-gon has $`k+1`$ vertices and $`k+1`$ faces, namely the base and
$`k`$ triangles. Stacking it replaces it by one $`(k+1)`$-vertex pyramid
and $`k`$ tetrahedra, adding $`4k`$ incidences and $`k`$ facets. There
is at least one tetrahedral facet. The remaining counts and
<a href="#eq:generalport" data-reference-type="eqref"
data-reference="eq:generalport">[eq:generalport]</a> follow from
Corollary <a href="#cor:polytocount" data-reference-type="ref"
data-reference="cor:polytocount">4</a>. ◻

</div>

<div id="lem:cap" class="lemma">

**Lemma 14** (Boundary accounting for the capped epigraph). *Fix a
normal periodic weighted-Delaunay mosaic with finitely many cell types,
convex lifting $`H`$, and densities $`(V,C,I)`$. For generic translated
cubes $`B_R`$ of side $`2R`$, and $`T_R>\max_{B_R}H`$, the capped
epigraph $`P_R`$ satisfies
``` math
(f_0(P_R),f_3(P_R),f_{03}(P_R))=(V,C,I)\operatorname{vol}(B_R)+O(R^2)
```
componentwise. The constants may depend on the fixed mosaic.*

</div>

<div class="proof">

*Proof.* Choose a common cell-diameter bound $`D`$. Only cells
intersecting the width-$`D`$ neighborhood of $`\partial B_R`$ can be
clipped. Periodicity and the finite list of cell types bound their
number by $`O(R^2)`$ and bound each cell’s numbers of faces and
incidences uniformly. Intersection with six halfspaces has bounded
combinatorial complexity per such cell: each new vertex is determined by
a face of that cell and a subset of the six clipping planes. Thus all
new lower vertices and their incidences with clipped lower facets
contribute $`O(R^2)`$. Interior vertices, facets and incidences are
unaltered. Counts in the cube differ from periodic density times its
volume by $`O(R^2)`$, by covering with fundamental domains and counting
those meeting its boundary.

There are at most six vertical facets. Their lower vertices are among
the just-counted boundary vertices; each is incident with at most six of
these facets. The top facet has the eight lifted cube corners, since
$`T_R`$ is strictly above the lower graph. The vertical facets have no
other vertices away from their lower boundary and those top corners.
Hence their additional vertices and vertex–facet incidences are
$`O(R^2)`$, not a volume-order term. The seven added facets themselves
contribute $`O(1)`$. These observations prove all three estimates,
including the incidence estimate. ◻

</div>

<div id="thm:equivalence" class="theorem">

**Theorem 15** (Asymptotic comparison). *The finite closures satisfy
``` math
\overline{\mathcal H_{\mathrm{pow}}}=\mathcal L_4.
```
Moreover, harmonic degree is unbounded on periodic
weighted-Delaunay/Laguerre mosaics if and only if $`\rho(P)`$ is
unbounded on convex four-polytopes.*

</div>

<div class="proof">

*Proof.* First let $`P_\ell`$ satisfy $`D_\ell=a_\ell+b_\ell\to\infty`$
and $`j_\ell/D_\ell\to H<\infty`$. Choose a facet with the fewest
vertices, so $`v_\ell\le j_\ell/b_\ell`$. Every three-polytope satisfies
$`f\le2v-4`$, and has a polygonal face with at most five sides:
$`e\le3f-6`$ implies average face size $`2e/f<6`$. Thus choose
$`k\le5`$.

Necessarily $`b_\ell\to\infty`$: with a bounded number of facets, every
vertex is determined by at least one independent four-tuple of facet
hyperplanes, so the number of vertices is bounded by
$`\binom{b_\ell}{4}`$. It follows that
``` math
\frac{v_\ell}{D_\ell}\le\frac{j_\ell/D_\ell}{b_\ell}\longrightarrow0,
 \qquad \frac{f_\ell}{D_\ell}\longrightarrow0.
```
The finite port cost in
<a href="#eq:generalport" data-reference-type="eqref"
data-reference="eq:generalport">[eq:generalport]</a> is therefore
negligible. Regular implantation gives harmonic degrees tending to
$`H`$. This proves
$`\mathcal L_4\subseteq\overline{\mathcal H_{\mathrm{pow}}}`$.

Conversely, let a periodic weighted-Delaunay mosaic have density triple
$`(V,C,I)`$, and let $`H(x)`$ be its convex lower-hull lifting. It is
quadratically periodic and has finitely many cell types. Restrict its
epigraph to a generic large cube $`B_R`$, and cap it above by a
horizontal plane at height $`T_R>\max_{B_R}H`$. This gives a convex
four-polytope
``` math
P_R=\{(x,t):x\in B_R,\ H(x)\le t\le T_R\}.
```
There are $`V\operatorname{vol}(B_R)+O(R^2)`$ lower vertices and
$`C\operatorname{vol}(B_R)+O(R^2)`$ lower facets. Clipping affects only
cells meeting the boundary layer, whose number and total incidence count
are $`O(R^2)`$. The six vertical side facets and the top facet add only
$`O(R^2)`$ incidences and vertices. Hence
``` math
f_0(P_R)=V\operatorname{vol}(B_R)+O(R^2),\quad
 f_3(P_R)=C\operatorname{vol}(B_R)+O(R^2),\quad
 f_{03}(P_R)=I\operatorname{vol}(B_R)+O(R^2).
```
Lemma <a href="#lem:cap" data-reference-type="ref"
data-reference="lem:cap">14</a> supplies the full boundary-incidence
accounting. Thus $`\rho(P_R)\to I/(V+C)`$. To check closedness
explicitly, let $`H_n\in\mathcal L_4`$ tend to a finite $`H`$. From a
sequence defining $`H_n`$, choose $`P_n`$ with
$`f_0(P_n)+f_3(P_n)\ge n`$ and $`|\rho(P_n)-H_n|<1/n`$. Then
$`\rho(P_n)\to H`$, so $`H\in\mathcal L_4`$. This proves the reverse
inclusion for closures.

If $`j/D\to\infty`$, the same minimum-facet construction gives a
harmonic degree bounded below by
``` math
\frac{j}{D+2j/b+5}.
```
Its reciprocal is at most $`D/j+2/b+5/j`$, which tends to zero. Thus
unbounded polytope complexity implies unbounded harmonic degree. The
capped-epigraph construction proves the converse. Bounded $`D`$ allows
only bounded flag counts, so no unbounded sequence is lost by imposing
$`D\to\infty`$. ◻

</div>

<div id="cor:lower" class="corollary">

**Corollary 16** (Lower bound in the periodic regular class). *Every
normal periodic weighted-Delaunay mosaic in the class defining
$`\mathcal H_{\mathrm{pow}}`$, and every corresponding Laguerre dual,
has $`\overline h\ge3`$.*

</div>

<div class="proof">

*Proof.* The established four-polytope inequality
``` math
f_{03}-3(f_0+f_3)\ge-10
```
is the nonnegativity of the second toric $`g`$-number; see , with the
general convex case attributed there to Kalai’s rigidity argument. Apply
it to the capped epigraph polytopes and divide by
$`\operatorname{vol}(B_R)`$. Taking the limit gives $`I\ge3(V+C)`$.
Duality preserves the harmonic degree. ◻

</div>

This corollary is restricted to the stated liftable periodic class. It
is not a proof of the conjectured strict lower bound for arbitrary
convex mosaics.
Theorem <a href="#thm:equivalence" data-reference-type="ref"
data-reference="thm:equivalence">15</a> explains precisely what a
complete upper-range classification in the periodic power-diagram class
would require. It does not supply a numerical maximum or decide whether
the range is unbounded.

# Verification and interpretation

The construction and its verification use exact rational arithmetic. The
finite certificate does not rely on numerical convex-hull tolerances, a
picture of a tiling, or incidence feasibility alone.

<div class="center">

| Check | Exact result |
|:---|:---|
| Projected deformed-cube positive-circuit rays | 66 total; 64 supporting facets; 2 strict redundant inequalities |
| Initial four-polytope face vector | $`(64,192,192,64)`$ |
| Twice-stacked face vector | $`(66,205,212,73)`$ |
| Template faces | 208 internal polygons; 4 boundary triangles |
| Template cells and incidences | 72 and 546 |
| Sum of exact template cell volumes | $`1/6`$ |
| Template regular lifting | Every cell is an exact strict lower facet |
| Periodic weighted realization | 373 sites, 432 Delaunay cells; 24 positive macro-face tests |
| Harmonic degree | $`468/115`$ |

</div>

The verifier reconstructs all nonnegative elimination circuits of
support at most three, checks every facet’s full equality set and every
vertex’s extremality, enumerates the face lattice by intersections,
replays the stackings, and checks the projection in exact barycentric
coordinates. It then checks interior-face multiplicities and
triangulates every polygonal cell boundary through face and cell
barycenters to obtain exact volumes. The weighted realization is checked
independently through its local convexity inequalities.

#### Why nonsimplicial cells matter.

For any periodic tetrahedral mosaic, $`I=4C`$, hence
$`\overline h=4C/(V+C)<4`$. Arbitrarily triangulating our nonsimplicial
cells therefore cannot preserve the counterexample’s harmonic degree.
The nonsimplicial incidence structure is substantive, not a drawing
convention.

#### Geological scope.

A universal statement about all normal convex face-to-face mosaics is
false. This does not say that the constructed highly structured cells
are typical rock fragments, that an ordinary fracture mechanism
generates them, or that empirical observations of a narrow band are
incorrect. Normality is a geometric size condition, not a stochastic
fracture law or a near-isotropy assumption. A physically motivated
replacement theorem must add explicit restrictions and test them;
convexity and face matching alone do not imply the proposed band.

#### Claim boundary.

The finite upper-band counterexample, periodic Laguerre realization,
explicit unbounded-degree families, interval inclusion $`(3,16)`$, and
regular-class asymptotic comparison are proved above. We do not claim an
exact description of $`S_3`$, a universal maximum of 16, the strict
lower bound $`\overline h>3`$ for all convex mosaics, or a
counterexample within unweighted Euclidean Voronoi mosaics. The code is
a reproducible exact check, not a proof-assistant formalization or an
independent human referee report.

# A self-contained rational four-polytope certificate

Set $`\varepsilon=1/2`$. In $`\mathbb R^6`$ impose
``` math
\begin{equation}
\label{eq:deformed}
 \varepsilon |x_k|\le
 \frac{2^{\binom{k}{2}}}{\varepsilon^{k-1}}
 -(-1)^k\sum_{j=1}^{k-1}\binom{k-2}{j-1}x_j,
 \qquad 1\le k\le6,
\end{equation}
```
where the sum is empty for $`k=1`$. This is a specialization of the
deformed-cube construction in ; we verify the specialization rather than
relying on an unspecified “sufficiently small” parameter.

For each sign vector $`\sigma\in\{-1,1\}^6`$, solve the equalities
recursively, selecting the sign $`\sigma_k`$ at step $`k`$. At every
prefix vertex the right side is strictly positive. Since it is affine in
the prefix variables, it remains positive throughout the prefix
polytope. Induction therefore shows that the feasible set is a
combinatorial six-cube and that the 64 recursively generated points are
all its vertices. Project to the last four coordinates and rescale them
by
``` math
(x_3,x_4,x_5,x_6)\mapsto
 \left(\frac{x_3}{64},\frac{x_4}{1024},\frac{x_5}{32768},\frac{x_6}{2097152}\right).
```
The result is the initial rational four-polytope used in the
certificate.

## Why the facet enumeration is complete

There are twelve signed inequalities in
<a href="#eq:deformed" data-reference-type="eqref"
data-reference="eq:deformed">[eq:deformed]</a>. Their first two
coefficients, the eliminated coordinates, are
``` math
(\pm\tfrac12,0),\quad(1,\pm\tfrac12),\quad
 (-1,-1),\quad(1,2),\quad(-1,-3),\quad(1,4),
```
with each of the last four vectors appearing twice. The nonnegative
dependence cone of these vectors consists of nonnegative multipliers
which cancel the first two coordinates. Its extreme rays have support at
most three: a minimal positive dependence in a two-dimensional vector
configuration has at most three members. Enumerating all subsets of
sizes one, two and three therefore enumerates all extreme elimination
rays.

For each ray, combine its original inequalities. Exact evaluation on the
64 projected vertices finds 66 rays: two resulting inequalities are
strict everywhere on the projected polytope, while each of the other 64
has exactly eight equality vertices spanning a three-dimensional affine
space. These 64 equality sets are distinct. Every projected facet is
exposed by an extreme elimination ray or a sum of rays exposing the same
facet, so the list is complete. This is also an immediate application of
the linear-inequality alternative underlying projection/elimination: the
projected set is described by all nonnegative combinations with
vanishing eliminated coordinates.

The verifier checks that the normals incident at every listed vertex
span four dimensions. It computes all face sets as intersections of the
facet vertex sets and obtains $`(64,192,192,64)`$. Within each facet it
obtains eight vertices, twelve edges and six quadrilateral faces; all
degrees are those of a cube. Thus no combinatorial or realizability
assumption is left unchecked in the finite example.

## Deterministic stacking and projection

Facets are ordered lexicographically by their vertex-index sets. Stack
first beyond the first facet. For any target facet, let $`z`$ be its
vertex barycenter and $`w`$ the mean of all current polytope vertices.
Choose the first number in $`1/2,1/4,1/8,\ldots`$ for which
``` math
p=z+\delta(z-w)
```
is strictly beneath every other facet. Since $`w`$ is interior and $`z`$
is in the target facet’s relative interior, such a choice exists and is
beyond the target facet. The verifier checks every sign explicitly.

The second target is the first square-pyramid facet containing the first
new vertex. The outer facet for the Schlegel projection is the first
tetrahedral facet containing the second new vertex. The viewpoint is
chosen by the same dyadic rule. Its exact projection formula is given in
Lemma <a href="#lem:schlegel" data-reference-type="ref"
data-reference="lem:schlegel">2</a>. An affine barycentric coordinate
map sends the four outer vertices, in their stored order, to
$`0,e_1,e_2,e_3`$.

The file `mosaic_certificate.json` contains all 64 initial vertices and
supporting halfspaces, elimination circuits, both stacking records, all
66 final four-dimensional vertices, all 73 facets, the viewpoint, the 66
three-dimensional template coordinates and their regular heights. Thus
the finite object can be regenerated without network access or a
polytope library.

# Reproduction instructions

Run from the package root, using Python with assertions enabled:

    python code/build_mosaic.py
    python code/verify_mosaic.py
    python code/verify_regular_realization.py
    python code/check_weighted_certificate.py
    python code/verify_abrasion.py
    python code/test_rejection.py

The only nonstandard runtime dependency is SymPy. The scripts reject
optimized Python execution, which would disable assertions. The final
three JSON reports and the rejection-test report are in `evidence/`. The
abrasion verifier belongs to the separate companion note. The package
manifest records SHA-256 hashes of the delivered files. Mathematical
assertions about infinite families and PDE evolution are established in
the manuscripts; the scripts certify the finite identities on which
their stated arguments rely.

#### Construction versus checking.

The historically named is a checked constructor: it regenerates and
overwrites the weighted-site payload. The separate is read-only and
compares the entire supplied payload to an exact checked reconstruction.
Rejection controls alter weights, lattice translations and cell
references, and verify input-byte preservation. Both routes share
reconstruction code and SymPy; this is not an independent implementation
of the infinite lower-hull proof.

<div class="thebibliography">

9 Rybnikov, K. (1999). Stresses and liftings of cell-complexes.
*Discrete & Computational Geometry, 21*, 481–517.
<https://doi.org/10.1007/PL00009434>. Domokos, G., & Lángi, Z. (2022).
On some average properties of convex mosaics. *Experimental Mathematics,
31*(3), 783–793. Published online 2019.
<https://doi.org/10.1080/10586458.2019.1691090>. Author version:
<https://arxiv.org/abs/1905.00721>.

Joswig, M., & Ziegler, G. M. (2000). Neighborly cubical polytopes.
*Discrete & Computational Geometry, 24*, 325–344.
<https://doi.org/10.1007/s004540010039>.
<https://arxiv.org/abs/math/9812033>.

Ziegler, G. M. (2002). Face numbers of 4-polytopes and 3-spheres. In
*Proceedings of the International Congress of Mathematicians, Beijing
2002* (Vol. III, pp. 625–634). Higher Education Press. Revised author
version (2003): <https://arxiv.org/abs/math/0208073>.

Ziegler, G. M. (2004). Projected products of polygons. *Electronic
Research Announcements of the American Mathematical Society, 10*,
122–134. <https://doi.org/10.1090/S1079-6762-04-00137-4>. Extended
abstract: <https://arxiv.org/abs/math/0407042> (arXiv metadata title:
*Projected Products of Polytopes*).

</div>
