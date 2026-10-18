"""Offline, source-only rights/provenance regression for public municipal/TUIK datasets.

No network, personal data, model calls, dataset rewriting or deployment.
"""
from __future__ import annotations

import csv
import json
import os
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
rows = list(csv.DictReader((ROOT / "sources.csv").open(encoding="utf-8-sig", newline="")))
snapshot = json.loads((ROOT / "validation_report.json").read_text(encoding="utf-8"))
assert len(rows) >= 5 and len({r["source_id"] for r in rows}) == len(rows)
assert snapshot["row_count"] == 30
assert snapshot["district_coverage"] == "30/30"
assert snapshot["checks"].get("no_composite_score") is True
assert snapshot["checks"].get("no_personal_data") is True

stale = []
for row in rows:
    source_id = row["source_id"]
    assert row["publisher"].strip(), source_id
    assert row["rights"].strip() and row["rights_url"].startswith("https://"), source_id
    origin = urlparse(row["source_url"])
    assert origin.scheme == "https" and origin.hostname in {
        "databrowser2.tuik.gov.tr", "acikveri.bizizmir.com"
    }, f"{source_id} source URL not approved"
    if source_id.startswith("tuik_"):
        assert "TUIK" in row["rights"] or "TurkStat" in row["rights"]
        assert urlparse(row["rights_url"]).hostname == "www.tuik.gov.tr"
    else:
        assert "CC BY 4.0" in row["rights"] or "IzBB Open Data License" in row["rights"], source_id
    observed = date.fromisoformat(row["snapshot_date"])
    age = (date.today() - observed).days
    assert age >= -1, source_id
    if age > 30:
        stale.append(f"{source_id}: {age} days")
if stale:
    print("STALE_SOURCE_SNAPSHOTS: " + "; ".join(stale))
    if os.environ.get("PUBLIC_STABLE") == "1":
        raise AssertionError("PUBLIC-STABLE release blocked on stale provenance")
print("PASS: TUIK rights preserved; IzBB attribution preserved; 30 district records; no composite score")
