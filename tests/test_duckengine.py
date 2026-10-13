import tempfile
from pathlib import Path
from duckengine.query import AnalyticsEngine

def test_in_memory_query():
    engine = AnalyticsEngine()
    res = engine.run_query("SELECT 42 AS answer, 'analytics' AS tag")
    assert res["row_count"] == 1
    assert res["rows"][0]["answer"] == 42

def test_csv_aggregation():
    engine = AnalyticsEngine()
    with tempfile.NamedTemporaryFile("w+", suffix=".csv", delete=False) as f:
        f.write("category,val\nA,10\nA,20\nB,30\n")
        f_path = f.name
    res = engine.run_query(f"SELECT category, SUM(val) AS total FROM '{f_path}' GROUP BY 1 ORDER BY 1")
    assert res["row_count"] == 2
    assert res["rows"][0]["total"] == 30
