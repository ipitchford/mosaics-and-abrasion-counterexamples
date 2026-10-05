# Problem 2: convex mosaics and centroidal abrasion

Evidence Press unrefereed candidate, version 1.1 — 5 October 2026.
This shared evidence package supports two separately identified papers: mosaics
(DOI 10.5281/zenodo.23167002) and abrasion (DOI 10.5281/zenodo.23167004).
See `AI_INDEX.md`, `ASSURANCE.md` and `REVIEW_RESPONSE.md` for the revised navigation,
verification boundaries and supplied-review dispositions.

## Main result

The proposed universal three-dimensional harmonic-degree band is false.
A rational, normal, periodic, face-to-face convex mosaic has

    V = 373, C = 432, I = 3276
    mean cells per vertex = I/V = 3276/373
    mean vertices per cell = I/C = 91/12
    harmonic degree = I/(V+C) = 468/115 = 4 + 8/115 > 4.

There is an exact periodic weighted-Delaunay realization and a rational weighted-site specification for its Laguerre (power-diagram) dual. The dual exchanges the two degree coordinates and has the same harmonic degree. This is not a claim about unweighted Euclidean Voronoi diagrams.

The main manuscript also proves: both mean-degree coordinates are separately unbounded in each dimension at least three; all harmonic degrees in (3,16) are attainable in dimension three, with rational values attainable periodically; and the closure of harmonic degrees in the periodic weighted-Delaunay/Laguerre class equals the finite asymptotic vertex–facet complexity limits of convex four-polytopes. The latter yields h >= 3 in that periodic regular class. It does not prove a universal strict lower bound or that 16 is a maximum.

## Abrasion companion

For epsilon = 1/100, the polynomial support function on the unit sphere

    s_mu(x,y,z) = 1 + epsilon*(y^2/2 + x^3*z/6 - 2*x*y^2*z + mu*x*z)

defines a uniformly strictly convex centrally symmetric body for |mu| <= 1. For every sufficiently small positive mu, inward mean-curvature flow creates two antipodal minimum–saddle pairs at positive time: the complete centroidal equilibrium count changes from 22 to 26. The result extends to every nontrivial nonnegative combination of mean and Gaussian curvature speeds, with a nonnegative constant speed added, and to an open set of asymmetric initial bodies.

A separate exact four-outcome probability law has zero means and zero covariance but positive expected equilibrium-count jump under the sign formula used in Domokos's moment-based stochastic argument. Corrected conditional-symmetry and Gaussian criteria are supplied.

The original published abrasion conjecture concerns an expected count. The source bundle incorrectly presents it as deterministic. The companion separates deterministic failure, distribution-free expectation failure, and failure of the stated moment inference. It does not refute every fully specified stochastic abrasion ensemble or the paper's distinct Assumption 2-A.

## Read and review

- `manuscript/mosaics.pdf` and `mosaics.tex`: main paper, including all count formulas, rational construction, tiling proofs, weighted realization and extensions.
- `manuscript/abrasion.pdf` and `abrasion.tex`: companion paper with the support-function proof, forward-time bifurcation, exact enumeration and probability correction.
- `evidence/mosaic_certificate.json`: full rational 4D polytope and 3D patch, supporting planes, face lists, stackings, regular lifting and incidence counts.
- `evidence/weighted_sites_certificate.json`: 373 rational sites/weights, lattice transform, and 432 weighted-Delaunay cell orbits.
- `evidence/*verification.json`, `rejection_tests.json`, `reproduction_receipt.json`: exact check results; corresponding logs are included.
- `RESEARCH_STATUS.json`, `AUDIT.md`, `SOURCES.md`: claim boundaries, proof checks, external inputs and prior-art distinctions.
- `SOURCE_PROBLEM.md`: the exact relevant supplied problem excerpt and input archive SHA-256.
- `MANIFEST.sha256`: hashes of the delivered package files, excluding the manifest itself.

## Reproduce

Install the dependency in `requirements.txt` when needed, then run:

    python code/reproduce.py

To verify the delivered file hashes before replay, use `shasum -a 256 -c MANIFEST.sha256` (or `sha256sum -c MANIFEST.sha256` on Linux). The manifest describes the delivered bytes; replay regenerates reports and their runtime measurements.

The replay itself does not access the network. It rebuilds the mosaic certificate, runs the separate rational verifier, constructs the weighted realization, checks its delivered payload read-only, verifies abrasion identities, and performs two positive controls, nine corrupted-certificate rejection tests and five optimized-execution guard tests. The scripts reject `python -O`, because that option disables assertion checks. Logs and JSON reports are regenerated locally. The weighted constructor and read-only checker share implementation code; the latter is not an independent infinite lower-hull proof.

The only nonstandard verification dependency is SymPy. No floating-point convex-hull library, SDP solver, remote model or private service is needed. The delivered replay used Python 3.13.5 and SymPy 1.14.0. Timings depend on hardware; they are recorded rather than promised.

To typeset, run `pdflatex` twice on each `.tex` file in `manuscript/`. The PDF build needs a standard LaTeX installation; it is not required for certificate verification. The manuscript sources and mathematical data are human-readable.

## Publication and novelty boundaries

The Schlegel insertion method and qualitative constructions with high mean tiling degrees appear in Ziegler's 2002 ICM article, Section 7. Neighborly cubical polytopes and projected products of polygons are established constructions, not discoveries of this package. The candidate contribution is their exact application to the later harmonic-degree conjecture, an explicit rational periodic Laguerre counterexample, and the stated refinements.

The general possibility of deterministic critical-point creation on surfaces was already acknowledged by Domokos. The companion's explicit globally convex centroidal construction, exact 22-to-26 count and finite probability obstruction are the claims to assess, not a claim to have discovered critical-point creation in general.

The package is a self-contained candidate with reproducible exact checks, not a proof-assistant formalization, an independent human review, or a certificate of priority. The mosaic builder and rational verifier are separate implementations prepared in the same research session. A focused primary-source search found the prior art discussed in `SOURCES.md` and `CITATION_AUDIT.md`; it cannot establish exhaustive novelty. The supplied review has been addressed internally. Independent specialist review and reproduction remain desirable future assurance, not assurance claimed by this publication.
