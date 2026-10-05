# Bounded adversarial audit and remaining gates

## Geometric falsifiers checked

**Formal counts without realizability.** Not accepted. The certificate has rational coordinates and all supporting planes. The separate verifier enumerates the elimination cone's extreme rays of support at most three and checks the complete projected-facet list, every equality set, vertex extremality and the full face lattices.

**Hidden nonconvex or overlapping cells.** The Schlegel proof supplies a convex subdivision. The verifier separately checks the strict lower lifting, exact internal face multiplicities and the total tetrahedral volume 1/6. These checks supplement the geometric projection proof; volume alone is not treated as a non-overlap proof.

**Nonmatching interfaces.** The template has only the four original boundary vertices and four original triangular boundary faces. Every inserted interior vertex is strictly inside the macro-tetrahedron. Affine copies therefore have identical unchanged boundary complexes.

**Incorrect boundary counting.** The periodic vertex count is 1 + 6*62 = 373, not 6*66. Cell and incidence counts are 6*72=432 and 6*546=3276. The harmonic degree is 3276/805=468/115.

**Failure of normality.** Each fixed periodic mosaic has a finite set of nondegenerate convex cell shapes. The minimum inradius is positive and maximum circumradius finite. The bounds need not be uniform across the asymptotic family.

**Unjustified Euclidean duality.** The package does not take an arbitrary geometric dual. It constructs a strictly convex periodic quadratic lifting with explicit rational matrix Q, rational Euclidean factor A and delta=1/256. All 24 directed macro-face tests are positive. The dual is the actual Laguerre diagram of the delivered weighted sites. No claim about unweighted Voronoi diagrams is made.

**Unjustified converse for arbitrary mosaics.** The epigraph-cap argument is restricted to periodic weighted-Delaunay mosaics. Non-liftable mosaics are not included in the equivalence theorem or regular-class lower bound.

**Manufactured novelty.** The manuscripts explicitly credit Schlegel insertion/high mean tiling degrees to Ziegler's 2002 discussion, neighborly cubical polytopes to Joswig–Ziegler, and projected products to Ziegler. The qualitative boundedness answer is not sold as newly invented.

## Abrasion falsifiers checked

**Local jet with no global convex body.** The polynomial support function is globally defined on S^2. The uniform curvature-radius lower bound is 9/10 for |mu|<=1; the paper proves the bound analytically. Central symmetry fixes the homogeneous centroid.

**Backward-parabolic continuation.** Not used. The bifurcation curve is obtained by varying the initial parameter mu and solving the fold equations along existing forward-time solutions. The positive birth time is mu/k+O(mu^2).

**Uncounted equilibria elsewhere.** Exact rational Sturm intervals cover all four roots of the critical quartic. Exceptional charts y=0, y=+/-1 and z=0 are handled explicitly. There are exactly 22 Morse points and two fold points at mu=0. Compactness and Morse persistence exclude unnoticed critical points for the perturbation and short flow.

**Symmetry-induced artifact.** The symmetric example has two ordinary local folds at the same time. Endpoint counts 22 and 26 persist on an open set of asymmetric initial bodies after recentering at the moving centroid. The open-set statement does not assert a fixed centroid for asymmetric perturbations.

**Stochastic versus deterministic substitution.** The actual published conjecture is about an expected count. The deterministic counterexample, open-set ensemble consequence, and moment-based stochastic counterexample are distinct statements. No unspecified ensemble is silently equated with a physical rock distribution.

**Covariance treated as independence.** The four-outcome law has EA=EB=EAB=0, but the sign expectation is -4/5. Conditional symmetry is given as a sufficient repair; marginal symmetry and zero covariance are not substituted for it. The paper also distinguishes nonpositive from strictly negative drift.

## Replay and mutation scope

`verify_mosaic.py` does not import the builder. It uses rational arithmetic and a separate implementation. The regularity constructor checks the global-convexity reduction through all periodic face types. The new read-only weighted checker shares that constructor's code, compares the entire payload and preserves its input bytes. `verify_abrasion.py` checks finite symbolic identities, not a formal parabolic PDE proof. Two positive controls pass; nine separate corruptions are rejected; five checked scripts reject Python's optimized mode. These tests are not exhaustive and were written within the producing workflow, not by an independent team.

## Further assurance, not claimed by this publication

1. Independent specialist review of the geometric transfer and PDE unfolding proofs.
2. Independent priority search, especially the implication of the earlier polytope/tiling literature for the later harmonic-degree conjecture and the precise stochastic correction.
3. The editorial decision is now implemented: the geometry paper and logically separate abrasion note have separate DOI and release identities, sharing this computational package.

The supplied review's proof-expansion requests are addressed in version 1.1; see `REVIEW_RESPONSE.md`. The first two items remain possible future independent assurance, not a claim that this internal publication process supplied it.

No exact classification of S3, no maximum h=16, no unweighted-Voronoi counterexample, and no proof of the general strict lower bound h>3 is claimed. The remaining upper-range issue in the periodic regular class has been reduced to a precise asymptotic four-polytope complexity question, rather than mislabeled as solved.
