import sqlite3
import os

DATADIR = os.path.dirname(os.path.join(__file__))
DB = os.path.join(DATADIR, 'UdaciousMusic.db')
INVOICELINE_SQL = os.path.join(DATADIR, 'invoiceline.sql')
conn = sqlite3.connect(DB)
cur = conn.cursor()

cur.executescript(INVOICELINE_SQL)

conn.commit()
conn.close()