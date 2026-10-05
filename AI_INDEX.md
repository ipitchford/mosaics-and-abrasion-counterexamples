# Agent entry point — two separate mathematical outputs

Anonymous; 1.1.0-candidate; unrefereed candidates. Shared repository: https://github.com/ipitchford/mosaics-and-abrasion-counterexamples.

## Claims and exact versions
- [manuscript/mosaics.tex](manuscript/mosaics.tex) and [PDF](manuscript/mosaics.pdf): DOI 10.5281/zenodo.23167002. Main counterexample: densities (373,432,3276), harmonic degree 468/115. Further written results concern interval filling and periodic regular-class/polytope limits; 16 is not claimed maximal.
- [manuscript/abrasion.tex](manuscript/abrasion.tex) and [PDF](manuscript/abrasion.pdf): DOI 10.5281/zenodo.23167004. Global convex support family, 22-to-26 forward-time equilibrium creation for sufficiently small positive mu; a distinct stochastic moment obstruction. No empirical ensemble claim.
- [CLAIMS.json](CLAIMS.json) separates finite checks from analytic dependencies.

## Replay and negative controls
Install [requirements.txt](requirements.txt), then run python code/reproduce.py in a disposable copy. This regenerates evidence reports and certificates. [code/check_weighted_certificate.py](code/check_weighted_certificate.py) instead checks a supplied weighted payload read-only, using exact deterministic reconstruction. It shares the constructor and SymPy, so is not independent reimplementation. [code/test_rejection.py](code/test_rejection.py) rejects nine payload corruptions and five optimized-Python invocations; assertions remain an explicit trust boundary.

## Evidence map
[evidence/mosaic_certificate.json](evidence/mosaic_certificate.json): rational vertices, halfspaces, stacking and Schlegel data. [evidence/weighted_sites_certificate.json](evidence/weighted_sites_certificate.json): 373 periodic sites and 432 cell orbits. [evidence/abrasion_verification.json](evidence/abrasion_verification.json): symbolic flow jets, Sturm isolation and moment arithmetic. [evidence/reproduction_receipt.json](evidence/reproduction_receipt.json): actual finite-run environment and logs.

## Limits, sources and review
[REVIEW_RESPONSE.md](REVIEW_RESPONSE.md) maps all supplied comments. [CITATION_AUDIT.md](CITATION_AUDIT.md) records the retrospective source check and novelty boundary. [ASSURANCE.md](ASSURANCE.md) distinguishes producer replay, prose proof and external assurance. [SOURCES.md](SOURCES.md) retains original source comparisons. [PROVENANCE.md](PROVENANCE.md) records original archive identity and revision roles.

## Reuse
[LICENSES.md](LICENSES.md) and [MANIFEST.sha256](MANIFEST.sha256) define rights and shipped bytes. No downloaded literature or private referee text is included. Open problems include the full convex-mosaic range, unbounded four-polytope complexity, unweighted Voronoi restrictions, and physically specified stochastic abrasion laws. Do not infer these from the finite examples.
