FROM python:3.13-slim AS builder

WORKDIR /build

COPY requirements.txt .

RUN pip install \
    --prefix=/install \
    --no-cache-dir \
    -r requirements.txt

COPY install_duckdb_extensions.py .

RUN python install_duckdb_extensions.py


FROM python:3.13-slim

COPY --from=builder /install /usr/local

COPY --from=builder /root/.duckdb /root/.duckdb

WORKDIR /app

RUN python -c "\
import duckdb; \
print(duckdb.sql('select * from duckdb_extensions()').fetchall())"

CMD ["python"]