# Link to the challenge
# https://www.linkedin.com/posts/crispo-mwangi-6ab49453_excel-excelchallenge-india-activity-7177529574765772800-fwMG/

import pandas as pd
from math import ceil

# Read the Excel file
file_path = 'Easy Excel Challenge 24th March.xlsx'
df = pd.read_excel(file_path, usecols='B:D', skiprows=2)

# Create a function to add custom year and quarter columns
def custom_year_quarter(col):
    q = ceil(col.month / 3)
    y = col.year
    if q < 2: return y - 1, 4
    else: return y, q - 1

# Data transformation and cleansing
df[['Year', 'Quarter']] = df['Date'].apply(custom_year_quarter).tolist()

df = pd.pivot_table(df, values='Sales', index='Year',columns='Quarter', aggfunc='sum', fill_value=0)
df = df.reset_index()
for i in range(1, 5):
    df[i] = df[i].map(lambda x: f'{x:,}')
df.columns.name = None
df.rename(columns={'Year': 'Financial Years'}, inplace=True)
df.replace('0', '', inplace=True)

# Print the required output
print(f"\n{' '*30}Financial Quarters\n{df}")

