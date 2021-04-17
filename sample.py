import pandas as pd
import numpy as np
import plotly.graph_objects as go
import csv


#TRL_abc
df = pd.read_csv('Mathscore.csv')
print(df.groupby('level')['attempt'].mean())

student_df = df.loc[df['student_id']=='TRL_abc']

figure = go.Figure(go.Bar(x=student_df.groupby('level')['attempt'].mean(), y=['Level 1', 'Level 2', 'Level 3', 'Level 4'], orientation='h'))
figure.show()


#TRL_xsl
df2 = pd.read_csv('Mathscore.csv')
print(df2.groupby('level')['atempt'].mean())

student_df2 = df2.loc[df2['student_id']=='TRL_xsl']

figure2 = go.Figure(go.Bar(x=student_df2.groupby('level')['attempt'].mean(),y=['Level 1','Level 2','Level 3','Level 4'],orientation='h'))
figure2.show()