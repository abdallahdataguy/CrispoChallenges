# Link to the challenge
# https://www.linkedin.com/posts/crispo-mwangi-6ab49453_excelchallenge-crispexcel-challenge-activity-7225712063354945539-pYxt/

import pandas as pd

# Create a function to get repeat customers
def get_repeat_customers(text):
    customers = [x.strip() for x in text.split(';')]
    repeat = [x for x in customers if customers.count(x) > 1]
    unique_repeat = sorted(set(repeat), key=lambda x: repeat.index(x))
    result = '; '.join(unique_repeat)
    return result

# Read the data range
file_path = 'Excel Challenge 4th August.xlsx'
df = pd.read_excel(file_path, usecols='B:C', skiprows=1, nrows=6)

# Perform data munging
df['Repeat Customers'] = df['Customers'].map(get_repeat_customers)
df = df[df['Repeat Customers'] > ''].reset_index(drop=True).iloc[:, 1:]

# Display the final results
df
