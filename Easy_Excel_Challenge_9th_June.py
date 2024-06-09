# Link to the challenge
# https://www.linkedin.com/posts/crispo-mwangi-6ab49453_excel-exceltips-crispexcel-activity-7205425884646813696--lBB/

import pandas as pd

# Read the Excel file
file_path = 'Easy Excel Challenge 9th June .xlsx'
df = pd.read_excel(file_path, usecols='C:F', skiprows=1)

# Perform data wrangling
values = []
for col in df.columns[1:]:
    values += list(df[col].unique())

df = pd.DataFrame([x for x in values if values.count(x) == 1], columns=['Students'])

# Display the final datset
df
