from preswald import text, query, plotly, connect, get_df, table
import pandas as pd
import plotly.express as px

# Connect and load dataset
connect()
df = get_df('marvel')

# UI Section
text("## Table of Marvel Characters")
table(df, title="All Marvel Characters")

# Visualization: Character count by Affiliation
text("## Characters by Affiliation")
affiliation_counts = df['Affiliation'].value_counts().reset_index()
affiliation_counts.columns = ['Affiliation', 'Count']

fig = px.bar(
    affiliation_counts,
    x='Affiliation',
    y='Count',
    title='Number of Characters per Affiliation',
    text='Count'
)
fig.update_layout(template='plotly_white')
plotly(fig)
