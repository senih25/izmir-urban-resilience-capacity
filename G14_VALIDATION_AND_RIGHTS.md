# GH-OPT-GPT2 G-14 — Dataset license and provenance gate

This repository distributes a **mixed-source public-interest data compilation**. Its source files, rights declarations and historic snapshots remain unchanged by this PR.

## Source rights — do not collapse into a single open-source code license

- **İzmir Büyükşehir Belediyesi** transit, hospital, market, emergency-assembly and district boundary inputs: follow the individual dataset terms and **CC BY 4.0 attribution** stated in `sources.csv` and `PROVENANCE_AND_RIGHTS.md`.
- **TÜİK / TurkStat ADNKS** population and annual-growth fields: subject to TÜİK's stated attribution-based legal notice, not automatically CC BY 4.0.
- `dataset-metadata.json` deliberately declares `"licenses":[{"name":"other"}]` to represent mixed rights. Do **not** replace it with MIT, CC0 or CC BY 4.0 without rights-holder review.
- Hackathon/Kaggle creation history, existing snapshot dates, and methodology limitations are preserved.

## Freshness and interpretive boundaries

- Source snapshot dates in `sources.csv` are **2026-08-23, 2026-08-24 and 2026-09-20**. They are collection evidence, **not** real-time municipal updates.
- `validation_report.json` is dated `2026-09-20`; validation passing again verifies committed table invariants only, not current source availability or data fitness for critical decisions.
- Zero source records do not mean real-world absence. Transit distances are straight-line approximations, not walking routes or ETAs.
- No total resilience, safety or investment ranking may be inferred from the raw capacity matrix.

## Independent CI acceptance

`python validate_release.py` checks the committed 30-row district dataset, declared totals, schema field names, metadata, notebook and cover artifact using **only local repository files**. Its path now resolves relative to the script rather than one developer's Windows computer. GitHub Actions runs Python 3.12 with `contents: read` and no network downloads or deployment.

**Unverified:** live public source freshness, source-rights changes after snapshots, full geographic coverage beyond committed samples, field-level accessibility, and independent official endorsement.

**Rollback:** close the G-14 draft PR or revert the validator, CI workflow, and this document. No dataset content or licensing state is altered.
