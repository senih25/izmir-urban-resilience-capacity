from pathlib import Path
import csv, json
# Validate the checked-out release snapshot without any writes or network requests.
root = Path(__file__).resolve().parent
with (root/"izmir_district_resilience_capacity.csv").open(encoding="utf-8-sig",newline="") as f:
    rows=list(csv.DictReader(f))
assert len(rows)==30
assert len({r["district"] for r in rows})==30
assert len({r["ibbs_code"] for r in rows})==30
def isum(k): return sum(int(float(r[k])) for r in rows)
assert isum("population_2025")==4504185
assert isum("hospital_records")==84
assert isum("street_market_records")==269
assert isum("assembly_area_records")==2382
assert isum("gtfs_stops_total")==11722
assert isum("weekday_departures")==867455
assert isum("rail_stops")==118
meta=json.loads((root/"dataset-metadata.json").read_text(encoding="utf-8"))
assert meta["licenses"]==[{"name":"other"}]
assert meta["id"]=="senihbayankulu/izmir-urban-resilience-capacity"
schema=meta["resources"][0]["schema"]["fields"]
assert [x["name"] for x in schema]==list(rows[0].keys())
assert (root/"dataset-cover-image.png").stat().st_size>10000
nb=json.loads((root/"izmir-resilience-capacity-atlas.ipynb").read_text(encoding="utf-8"))
assert nb["nbformat"]==4
km=json.loads((root/"kernel-metadata.json").read_text(encoding="utf-8"))
assert km["dataset_sources"]==["senihbayankulu/izmir-urban-resilience-capacity"]
print("VALIDATOR=PASS")
print("ROWS=30 DISTRICTS=30 POPULATION_2025=4504185")
print("HOSPITALS=84 MARKETS=269 ASSEMBLY=2382")
print("GTFS_STOPS=11722 WEEKDAY_DEPARTURES=867455 RAIL_STOPS=118")
