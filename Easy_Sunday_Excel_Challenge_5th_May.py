# Link to the challenge
# https://www.linkedin.com/posts/crispo-mwangi-6ab49453_excel-excelchallenge-exceltips-activity-7192749873375432704-3U5Y/

import pandas as pd

# Read the Excel file
file_path = 'Easy Sunday Excel Challenge 5th May.xlsx'
df = pd.read_excel(file_path, usecols='B:D', skiprows=1)

# Perform data transformation and cleansing
df['Quarter'] = df.Date.dt.quarter

values = 0
progress = 0
for i in df.index:
    if i == 0 and df.iat[i, 2] > 0:
        progress = 1
    elif i > 0 and df.iat[i, 2] > 0 and df.iat[i, 3] != df.iat[i - 1, 3]:
        progress = 1
    elif i > 0 and df.iat[i, 2] > 0 and df.iat[i, 3] == df.iat[i - 1, 3]:
        progress += 1
    else:
        progress = 0
    if progress == 3:
        values += 1
        progress = 0

# Display the output
print(values)
