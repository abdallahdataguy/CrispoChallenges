# Link to the challenge
# https://www.linkedin.com/posts/crispo-mwangi-6ab49453_excel-excelchallenge-crispexcel-activity-7215587842582839296-qvV4/

# Read the data range
df = xl("B3:B20", headers=True)

# Perform data wrangling
cond = ((df['SALES'].shift(1) == 'NEW ORDER') 
        + (df['SALES'].shift(-1) == 'NEW ORDER'))
df = df[['SALES']][cond].reset_index(drop=True)
df = df.rename(columns={'SALES': 'Before & After Dates'})

# Display the final dataset
df
