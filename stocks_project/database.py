from io import BytesIO
import requests
import pandas as pd
from github import Github
import os


# updated database with recent matches from github
def get_df():
    url_df = 'https://github.com/alanhassan/stocks_panel/blob/main/df.csv?raw=true'
    data = requests.get(url_df).content
    df = pd.read_csv(BytesIO(data))
    df = df.sort_values('Empresa')
    df = df[df['Setor'].notnull()]
    df['Patrim. Líq'] = df['Patrim. Líq'].apply(lambda x: f"{x:,.0f}")
    return df

df = get_df()