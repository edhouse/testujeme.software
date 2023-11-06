import pandas as pd
import plotly.express as px
import streamlit as st

# Set column names
columns_results = [
        'Timestamp',
        'MyApp.Server.exe RAM',
        'MyApp.Client.exe RAM',
        'Total free RAM',
        'CPU Time',
        'python.exe RAM'
    ]
columns_notes = ['Timestamp', 'Note']

# Read the results from the TSV file
results = pd.read_csv("./perfmon-results.tsv", sep='\t', header=0, names=columns_results)

# Read the notes from the TSV file
notes = pd.read_csv("./perfmon-notes.tsv", sep='\t', header=0, names=columns_notes)

# Merge the results and notes
results_notes = pd.concat([results, notes])
results_notes = results_notes.sort_values(by=['Timestamp'])

# Streamlit page config
st.set_page_config(
    page_title="Performance Test",
    page_icon=":bar_chart:"
)

st.markdown("# Performance test results with notes")

# Performance results
fig = px.line(results_notes, x='Timestamp', y=['MyApp.Server.exe RAM', 'MyApp.Client.exe RAM'], title="Selected data & notes")

# Notes
for index, row in results_notes.iterrows():
    note = str(row['Note']).strip()

    if note != 'nan':
        
        # Annotation
        fig.add_annotation(
            x=row['Timestamp'], # x position
            y=0, # y position
            ay=30, # annotation position
            text=note) # annotation text
        
        # Red dashed line
        fig.add_vline(x=row['Timestamp'], line_width=0.5, line_dash="dot", line_color="red", opacity=0.5)

# Plot figure
st.plotly_chart(fig)