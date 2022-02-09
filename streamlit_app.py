from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
# import nashpy as nash
from gsheetsdb import connect
import numpy as np


"""
# Applied Game Theory Final Project
Andrew Chan
"""

"""
    ## Summary
    Compare metrics between different forecasting methods

    Link to paper
"""

"""
    ## Methodology 
    
"""

tic_option = st.selectbox(
    'Select Ticker Symbol',
    ('GOOG','AAPL','MSFT'))

st.write('You selected:', tic_option)


# LOAD DATA
# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows
if tic_option == 'GOOG':
    sheet_url = st.secrets["gsheets_url_goog"]
elif tic_option == 'AAPL':
    sheet_url = st.secrets["gsheets_url_aapl"]
else:
    sheet_url = st.secrets["gsheets_url_msft"]

rows = run_query(f'SELECT * FROM "{sheet_url}"')

dates = []
prices = []
for row in rows:
  dates.append(row.Date)
  prices.append(row.Close)
st.write('dates',dates)
st.write('prices',prices)

# https://www.kite.com/python/answers/how-to-create-pandas-dataframe-from-a-numpy-array-in-python
df_data = pd.DataFrame({'dates':np.array(dates),'prices':np.array(prices)})

st.write(df_data.iloc[-10])

time = np.array(dates)
series = np.array(prices)

st.write(f'Selected option: `{tic_option}`')



# A = [[1, -1], [-1, 1]]
# B = [[-1, 1], [1, -1]]
# matching_pennies = nash.Game(A, B)
# st.write(f'```{matching_pennies}```')
