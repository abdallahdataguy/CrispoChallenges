# Link to the challenge
# https://www.linkedin.com/posts/crispo-mwangi-6ab49453_easy-sunday-excel-challenge-extract-the-activity-7203076251522076673-fivB/

import pandas as pd
import re

# Read the Excel file
file_path = 'Easy Excel Challenge 2nd June.xlsx'
df = pd.read_excel(file_path, usecols='C:D', skiprows=1, nrows=6)
df = df.replace(float('nan'), '')

# Perform data wrangling
def extract_last_order(text):
    matches = re.findall('[a-zA-Z](#?\d+)', text)
    return matches[-1] if matches else ''
    
df['My Last Correct Order'] = df.iloc[:, 0].map(extract_last_order)

# Display the finalresults
df
