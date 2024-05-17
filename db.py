from sqlalchemy import create_engine
import pandas as pd

engine=create_engine('sqlite:///database.db')
conn=engine.connect()

df=pd.read_csv('data/source.csv')
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html
# creates schema and inserts records
df.to_sql('data_table', con=conn)

conn.close()