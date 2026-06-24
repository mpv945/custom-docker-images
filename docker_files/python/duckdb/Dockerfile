FROM python:3.13-slim AS builder

WORKDIR /build

COPY requirements.txt .
# pip install --prefix=/install 安装到了： /install/lib/python3.13/site-packages 而不是当前 Python 的：/usr/local/lib/python3.13/site-packages
RUN pip install \
    --prefix=/install \
    --no-cache-dir \
    -r requirements.txt

COPY scripts/install_duckdb_extensions.py .

#RUN python install_duckdb_extensions.py
RUN PYTHONPATH=/install/lib/python3.13/site-packages \
    python install_duckdb_extensions.py


FROM python:3.13-slim

COPY --from=builder /install /usr/local

COPY --from=builder /root/.duckdb /root/.duckdb

WORKDIR /app

#RUN python -c "\
#import duckdb; \
#print(duckdb.sql('select * from duckdb_extensions()').fetchall())"

CMD ["python"]