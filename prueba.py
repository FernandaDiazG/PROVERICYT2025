from sklearn.ensemble import RandomForestClassifier 
from sklearn.datasets import make_classification
import pandas as pd
import sqlite3
from contextlib import closing

db = "test 2.db"

def get_events(uid:int):
    with closing(sqlite3.connect(db)) as conn:
        return pd.read_sql(
            f"SELECT * FROM events_{uid}", conn
        )

def get_session(uid:int, start:int, stop:int):
    with closing(sqlite3.connect(db)) as conn:
        return pd.read_sql(
            f"SELECT * FROM session_{uid} LIMIT {stop-start} OFFSET {start}", conn
        )

events = get_events(20241003152320)
events.head()

session = get_session(20241003152320, events.iloc[0, 0], events.iloc[-1,0])
session.head()

X = session[['delta0','theta0','low_alpha0','high_alpha0','low_beta0','high_beta0','low_gamma0','high_gamma0']]
y = session[['attention0','meditation0']]