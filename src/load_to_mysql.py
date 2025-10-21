import pandas as pd
from sqlalchemy import create_engine
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config.db_config as db

df = pd.read_csv('data/earthquake_data_tsunami.csv')
print(df.head())

engine = create_engine(f'mysql+pymysql://{db.user}:{db.password}@{db.host}:{db.port}/{db.database}')

print(df.isnull().sum())
df.drop_duplicates(inplace=True)
print("Data cleaned: duplicates removed and missing values counted.")
print(df.dtypes)

print(df['magnitude'].describe())
df=df[(df['magnitude']>=0)&(df['magnitude']<=10)]

df=df[(df['latitude'].between(-90,90)& (df['longitude'].between(-180,180)))]
print("Data validation completed: magnitude, latitude, and longitude values are within valid ranges.")