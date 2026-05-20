import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('digital_burnout_productivity_dataset_5M (1).csv')

username = 'YOUR_USER_NAME'
password = 'YOUR_PASSWORD'
host = 'HOST'
port = 'PORT'
database = 'YOUR_NAME_DATABASE'

engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

df.to_sql(
    "YOUR_TABLE_NAME",
    engine,
    if_exists="replace",
    index=False
)
