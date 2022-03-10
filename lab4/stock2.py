import requests
import json
import pandas as pd
import sys

url = "https://yfapi.net/v6/finance/quote"

ticker_symbols = sys.argv
querystring = {"symbols":ticker_symbols}

headers = {
    'x-api-key': "insert here"
}

response = requests.request("GET", url, headers=headers, params=querystring)
results = json.loads(response.text)
#print(response.text)


df = (pd.DataFrame.from_dict(results['quoteResponse']['result']))
df = df[['symbol', 'longName', 'regularMarketPrice']]
df = df.fillna("NOT FOUND")
#print(df)
#print(df.columns)
#print(df)

df_string = df[['symbol', 'longName', 'regularMarketPrice']].to_string(index=False)

print(df_string)
