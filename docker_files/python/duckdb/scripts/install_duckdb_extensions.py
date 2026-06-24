import duckdb

extensions = [
    "httpfs",
    "postgres",
    "mysql",
    "iceberg",
    "delta",
    "json",
    "parquet"
]

conn = duckdb.connect()

for ext in extensions:
    try:
        print(f"Installing {ext}")
        conn.execute(f"INSTALL {ext}")
        conn.execute(f"LOAD {ext}")
    except Exception as e:
        print(f"{ext}: {e}")

conn.close()