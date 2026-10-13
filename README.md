# FastDuck Analytics &mdash; In-Process Analytical SQL Engine

[![DuckDB](https://img.shields.io/badge/DuckDB-Vectorized-yellow.svg)](https://duckdb.org)
[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**FastDuck Analytics** is a high-velocity analytical micro-engine powered by DuckDB. It allows developers to query millions of records across CSV, Parquet, JSON, and SQLite files in sub-second times with zero server footprint.

---

## ⚡ Performance Metric

- **Vectorized Execution**: 10x-50x speedup over standard Python loops or SQLite.
- **Zero External Server**: Embeds directly into Python microservices without running a separate database daemon.

---

## 🚀 Quick Example

```python
from duckengine.query import AnalyticsEngine

engine = AnalyticsEngine()
result = engine.run_query(
    "SELECT category, COUNT(*), AVG(price) FROM 'data/sales.parquet' GROUP BY 1"
)

print(f"Aggregated {result['row_count']} rows in {result['elapsed_ms']}ms")
```

Developed by [Leonard Johnson](https://github.com/hiper728) &bull; [Portfolio](https://hiper728.github.io)
