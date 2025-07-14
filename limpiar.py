import pandas as pd
import numpy as np
import sqlite3

with closing(sqlite3.connect('test 2.db')) as conn:
    df = pd.read_sql(,conn:sqlite3)

df_d = df.loc[df['signal_strength'] == 0]

df_d.to_csv('datos.db', index=False)