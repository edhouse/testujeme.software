import pandas as pd
import plotly.express as px
import streamlit as st

# Set column names
columns = [
        'Timestamp',
        'MyApp.Server.exe RAM',
        'MyApp.Client.exe RAM',
        'Total free RAM',
        'CPU Time',
        'python.exe RAM'
    ]

# Read the results from the TSV file
results = pd.read_csv("./perfmon-results.tsv", sep='\t', header=0, names=columns, )
results = results.sort_values(by=['Timestamp'])

# Streamlit page config
st.set_page_config(
    page_title="Performance Test",
    page_icon=":bar_chart:"
)

st.markdown("# Performance test results")

# Plot figure
fig = px.line(results, x=columns[0], y=columns[1:], title="All data")
st.plotly_chart(fig)

# Plot figure
fig = px.line(results, x=columns[0], y=['MyApp.Server.exe RAM', 'MyApp.Client.exe RAM'], title="Selected data")
st.plotly_chart(fig)
