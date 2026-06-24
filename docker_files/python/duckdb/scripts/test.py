import duckdb

conn = duckdb.connect()

conn.execute("LOAD httpfs")
conn.execute("LOAD aws")

conn.execute("""
CREATE SECRET (
    TYPE S3,
    KEY_ID 'admin',
    SECRET 'password',
    REGION 'us-east-1',
    ENDPOINT 'ozone-s3.company.com'
)
""")


# SELECT *
# FROM read_parquet(
# 's3://warehouse/test/*.parquet'
# );