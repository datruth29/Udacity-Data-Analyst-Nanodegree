import sqlite3
import os

DATADIR = os.path.dirname(os.path.join(__file__))
DB = os.path.join(DATADIR, 'UdaciousMusic.db')

conn = sqlite3.connect(DB)
cur = conn.cursor()