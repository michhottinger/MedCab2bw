
import pandas as pd

#import the data from github where it is saved
url = 'https://github.com/michhottinger/MedCab2bw/blob/master/cannabis.csv?raw=true'
df = pd.read_csv(url)
df.head(5)

url2 = 'https://raw.githubusercontent.com/DNason1999/simple_repository/master/df.csv'
df2 = pd.read_csv(url2)

#clean the first source of data
df_1 = df[['Strain', 'Rating', 'Description']].sort_values('Strain', ascending=True)
df_1['Strain']=df_1['Strain'] = df['Strain'].str.replace('-', ' ')

#Reconfigure the second set of data
df2t = df2.T

#relabel and index reset second dataset
df_2 = df2t.reset_index().rename(columns={'index': 'Strain', 1: 'race', 2: 'flavors', 3: 'effects', 4: 'positive', 5: 'negative', 6: 'medical'}).drop([0])

#join the datasets
df_join = df_2.set_index('Strain').join(df_1.set_index('Strain'))
df_final = df_join.drop([0], axis=1)
