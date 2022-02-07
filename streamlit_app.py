from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import nashpy as nash


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
hello = 42
st.write(f'Selected option: `{hello}`')

A = [[1, -1], [-1, 1]]
B = [[-1, 1], [1, -1]]
matching_pennies = nash.Game(A, B)
st.write(matching_pennies)
