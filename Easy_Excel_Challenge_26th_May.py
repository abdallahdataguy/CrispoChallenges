# Link to the challenge
# https://www.linkedin.com/posts/crispo-mwangi-6ab49453_excel-india-hr-activity-7200360000685244417-WdhX/

import pandas as pd

# Read the Excel file
file_path = 'Easy Excel Challenge 26th May.xlsx'
df = pd.read_excel(file_path, usecols='C:E', skiprows=1)

# Perform data wrangling
df = df.dropna().tail(5).reset_index(drop=True)
df['Date'] = df['Date'].dt.strftime('%d/%m/%Y')
df['Amount'] = df['Amount'].map(lambda x: f'${x:,.0f}')

# Display the final results
df
