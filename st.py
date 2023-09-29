import pandas as pd
import numpy as np
import streamlit as st

df = pd.read_excel('https://github.com/basketking/wch/blob/main/results_individuals.xlsx?raw=true')
df_group = df.groupby('playerAName').agg({
    'associationPlayer_A': 'count',
    'pointTotal_A': [('sum_pointTotal_A', 'sum'), ('average_pointTotal_A', 'mean')],
    'pointTotal_X': [('sum_pointTotal_X', 'sum'), ('average_pointTotal_X', 'mean')],
    'setsWon_A': [('sum_setsWon_A', 'sum'), ('average_setsWon_A', 'mean')],
    'setsWon_A': [('sum_setsWon_X', 'sum'), ('average_setsWon_X', 'mean')],
})
# df_group.columns = df_group.columns.get_level_values(0)

st.table(df_group)

