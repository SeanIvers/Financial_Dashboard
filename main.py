import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from alpha_vantage.timeseries import TimeSeries

key = 'DLFYKTONSQFO1YSI'
# https://github.com/RomelTorres/alpha_vantage

ts = TimeSeries(key, output_format='pandas')
# Pulling from the Alpha Vantage API
ttm_data, ttm_meta_data = ts.get_intraday(symbol='TTM', interval='1min', outputsize='compact')
df = ttm_data.iloc[:50].copy()
df=df.transpose()
df.rename(index={"1. open":"open", "2. high":"high", "3. low":"low",
                "4. close":"close", "5. volume":"volume"}, inplace=True)
df=df.reset_index().rename(columns={'index': 'indicator'})
df = pd.melt(df, id_vars=['indicator'], var_name='date', value_name='rate')
df = df[df['indicator'] != 'volume']