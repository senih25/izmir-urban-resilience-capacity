# Methodology

## Product question
How can Izmir's 30 districts be compared using transparent, non-ranking public-service capacity indicators while preserving source provenance and uncertainty?

## Evidence families
1. Population: TUIK ADNKS 2024-2025.
2. Transit: verified district-level features from official IzBB and municipal-operator open-data feeds.
3. Everyday and health services: IzBB hospital and street-market sources.
4. Emergency preparedness context: IzBB emergency assembly-area source.

## Normalization
Raw source counts are retained. Additional denominator-normalized fields use 2025 district population:
- hospitals per 100,000 residents
- markets per 10,000 residents
- emergency assembly areas per 10,000 residents
- GTFS stops per 10,000 residents
- representative-weekday departures per 1,000 residents
- rail stops per 100,000 residents

These are arithmetic normalizations only. No learned model, hidden weighting or composite index is used.

## Transit semantics
The transit feature pipeline uses a representative weekday service model. Median nearest-stop and nearest-rail distances are straight-line distances from neighborhood representative points. They describe settlement-core context and must not be described as district-wide walking access.

## Zero records
A zero in a facility-record count means that the published source snapshot returned no record after normalization. It does not prove real-world absence. Explicit source_zero_record flags are therefore included.

## Why no resilience score?
A single score would require normative weights across hospitals, markets, emergency assembly capacity, transit and population. Those weights are not objectively identified by the sources. Publishing components separately is more auditable and reusable.

## Reproducibility boundary
This is a dated analytical snapshot. Original sources may update independently. Preserve snapshot dates and source registry when extending the analysis.
