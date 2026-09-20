# Data Dictionary

Primary file: izmir_district_resilience_capacity.csv

| Field | Meaning |
|---|---|
| district | Official Izmir district name. |
| ibbs_code | TUIK district identity code. |
| population_2024 | Official ADNKS population count for 2024. |
| population_2025 | Official ADNKS population count for 2025. |
| population_delta_persons | Population 2025 minus population 2024. |
| official_growth_rate_per_mille_2025 | TUIK continuous annual growth rate in per mille. |
| hospital_records | Hospital records in the IzBB source snapshot. |
| street_market_records | Street-market records in the IzBB source snapshot. |
| assembly_area_records | Emergency assembly-area records in the IzBB source snapshot. |
| gtfs_stops_total | District-assigned public-transport stop records. |
| rail_stops | District-assigned rail-stop records. |
| ferry_access | Whether ferry access is recorded in the transit feature pipeline. |
| route_diversity | Distinct route context in the representative-weekday model. |
| weekday_departures | Representative-weekday scheduled departures assigned to district. |
| rail_departures | Representative-weekday rail departures; blank when no rail record exists. |
| neighborhood_count | Neighborhood representative points in district aggregation. |
| median_neighborhood_nearest_stop_m | Median straight-line distance from neighborhood representative points to nearest transit stop. |
| median_neighborhood_nearest_rail_m | Median straight-line distance from neighborhood representative points to nearest rail stop. |
| hospital_records_per_100k | Hospital source records per 100,000 2025 residents. |
| street_markets_per_10k | Street-market source records per 10,000 2025 residents. |
| assembly_areas_per_10k | Assembly-area source records per 10,000 2025 residents. |
| gtfs_stops_per_10k | Transit-stop records per 10,000 2025 residents. |
| weekday_departures_per_1k | Weekday departures per 1,000 2025 residents. |
| rail_stops_per_100k | Rail-stop records per 100,000 2025 residents. |
| hospital_source_zero_record | True when source snapshot returned zero hospital records; not proof of real-world absence. |
| market_source_zero_record | True when source snapshot returned zero market records; not proof of real-world absence. |
| has_rail_stop_record | True when the transit feature set contains at least one rail-stop record. |

## Guardrails

Zero source records are not proof of absence. Transit distances are straight-line proxies, not walking time. Per-capita metrics are context, not quality or safety scores. No composite resilience, livability or investment ranking is included.
