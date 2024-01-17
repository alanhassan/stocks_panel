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

    return df

df = get_df()