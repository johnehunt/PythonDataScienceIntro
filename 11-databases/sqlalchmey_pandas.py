import pandas as pd
import sqlalchemy as sqla

db = sqla.create_engine('mysql://user:password@localhost/database')

# Convert database data into DataFrame
df = pd.read_sql('SELECT * FROM readings',db)
print(df.to_string())
