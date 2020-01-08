import pandas as pd
from sqlalchemy import create_engine

d = pd.read_csv('https://raw.githubusercontent.com/DNason1999/simple_repository/master/df_merged.csv')
df = pd.DataFrame(data=d)
#sql method

engine = create_engine('sqlite:///db.sqlite', echo=False)
df.to_sql('Strain', con=engine)
print(engine.execute("SELECT * FROM Strain").fetchall())
