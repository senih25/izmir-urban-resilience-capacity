# Izmir Urban Resilience & Essential Services Atlas

A district-level, evidence-first public-interest dataset for Izmir, Turkiye.

## What is new
Instead of publishing another raw facility list, this product combines population, public transport, hospitals, street markets and emergency assembly areas into one 30-district analytical table.

The main contribution is not a ranking. It is an explainable capacity matrix:
- raw source-record counts
- population-normalized capacity measures
- transit service context
- straight-line neighborhood-to-transit proxies
- explicit zero-record and interpretation guards
- source-by-source rights and provenance

## Coverage
- 30 / 30 Izmir districts
- 2025 population total represented: 4,504,185
- 84 hospital records
- 269 street-market records
- 2,382 emergency assembly-area records
- 11,722 transit-stop records in the district feature pipeline
- 867,455 representative-weekday departures
- 118 rail-stop records

## Rights and data freshness

This public dataset combines **separately sourced** TÜİK / TurkStat and İzmir Büyükşehir Belediyesi (İzBB) records. The TÜİK reuse notice and IzBB open-data/CC BY 4.0 attribution have **different legal conditions**; no single blanket open-source or CC BY license is inferred for the complete repository. Kaggle license metadata remains `other` pending rights-holder review. See [PROVENANCE_AND_RIGHTS.md](PROVENANCE_AND_RIGHTS.md) and [sources.csv](sources.csv).

The source dates in `sources.csv` are historical retrieval evidence, **not** current service availability. The offline G-14 CI reports stale snapshots while the dataset is an evidence-oriented public release, and `PUBLIC_STABLE=1` rejects snapshots older than the 30-day provisional threshold. No district quality/safety score or official ranking is claimed.

## Start here
Primary table: izmir_district_resilience_capacity.csv

Then read DATA_DICTIONARY.md, METHODOLOGY.md, PROVENANCE_AND_RIGHTS.md, sources.csv and validation_report.json.

## Important: this is not a district ranking
There is no composite resilience, quality, safety, livability or investment score.

A district with fewer records may still have services missing from the source. A district with many departures may still have accessibility barriers not captured by straight-line distance. Use each field with its stated semantics.

## Rights
This is a mixed-source compilation.
- Izmir Metropolitan Municipality open-data inputs retain their source-specific CC BY 4.0 attribution requirements.
- TurkStat/TUIK data is reused with source attribution under the reuse statement in the TUIK Legal Notice.

See PROVENANCE_AND_RIGHTS.md and sources.csv for source-specific rights and URLs.
