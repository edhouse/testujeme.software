import pandas as pd
import streamlit as st

st.title("Test results")
df = pd.read_csv("test-results.csv")

versions = []
i = 0
for version in df.columns:
	if i > 0:
		versions.append(version)
	i += 1

def colorize(val):
	if val == "Passed":
		return f'background-color: green; color:white'
	if val == "Failed":
		return f'background-color: red; color:white'
	else:
		return None
	

filter_result = st.multiselect(
	label='Result',
	options=('Passed', 'Failed'),
	default=('Passed', 'Failed')
	)
filer_version = st.multiselect(
	label='Version',
	options=versions,
	default=versions)

filer_version.append("Test")
df = df.loc[:, df.columns.isin(filer_version)]

num = -1 * len(versions)
df = df[df.iloc[:,num:].isin(filter_result).any(axis=1)]

st.dataframe(df.style.applymap(colorize, subset=df.columns))