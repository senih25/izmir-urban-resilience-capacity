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
