import duckdb
import time
from typing import Dict, Any, List

class AnalyticsEngine:
    def __init__(self, db_path: str = ":memory:"):
        self.con = duckdb.connect(database=db_path)

    def run_query(self, sql: str, max_rows: int = 500) -> Dict[str, Any]:
        t0 = time.perf_counter()
        rel = self.con.execute(sql)
        cols = [d[0] for d in rel.description] if rel.description else []
        rows = rel.fetchmany(max_rows)
        elapsed_ms = round((time.perf_counter() - t0) * 1000, 2)
        return {
            "elapsed_ms": elapsed_ms,
            "columns": cols,
            "row_count": len(rows),
            "rows": [dict(zip(cols, r)) for r in rows],
        }

    def summarize_dataset(self, file_path: str) -> Dict[str, Any]:
        escaped = file_path.replace("\\", "/").replace("'", "''")
        count = self.con.execute(f"SELECT COUNT(*) FROM '{escaped}'").fetchone()[0]
        return {
            "file": file_path,
            "total_rows": count,
        }
