import os, psycopg2
from psycopg2 import sql

DB_NAME = "test_db"
TABLE_NAME = "test_table"

URL = os.environ.get("DATABASE_URL")
conn = psycopg2.connect(URL)
conn.autocommit = True
with conn.cursor() as cur:
    # create database if it doesn't exist
    cur.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{DB_NAME}';")
    exists = cur.fetchone()
    if not exists:
        cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))
    # close the connection
    cur.close()
conn.close()

NEW_URL = URL.rsplit("/", 1)[0] + f"/{DB_NAME}"
conn = None
conn = psycopg2.connect(NEW_URL)
with conn.cursor() as cur:
    # create table if it doesn't exist
    cur.execute(sql.SQL("CREATE TABLE IF NOT EXISTS {} (id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, company VARCHAR(100), added TIMESTAMP DEFAULT CURRENT_TIMESTAMP)").format(sql.Identifier(TABLE_NAME)))
    # insert new rows (with data from environment variables)
    insert_query = sql.SQL("INSERT INTO {} (name, company) VALUES (%s, %s)").format(sql.Identifier(TABLE_NAME))
    DATA_TO_INSERT = [
        (os.environ.get("PASS_VALUE_NAME"), os.environ.get("PASS_VALUE_COMPANY")),
        (os.environ.get("PASS_VALUE_NAME2"), os.environ.get("PASS_VALUE_COMPANY2"))
    ]
    cur.executemany(insert_query, DATA_TO_INSERT)
    # commit changes
    conn.commit()
    # check inserted rows
    cur.execute(sql.SQL("SELECT * FROM {}").format(sql.Identifier(TABLE_NAME)))
    rows = cur.fetchall()
    for row in rows:
        print(row)
conn.close()