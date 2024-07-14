# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/crispo-mwangi-6ab49453_excelchallenge-crispexcel-excel-activity-7218109503303479296-Ygt3/

# Read the data range
df = xl("B2:D8", headers=True)

# Perform data wrangling
df['Customers'] = df['Customers'].str.split("; ")
df['Orders'] = df['Orders'].str.split("; ")
df = df.explode(column=['Customers', 'Orders'])
df['Orders'] = df['Orders'].astype(int)
df = df.pivot(
    columns='Customers', 
    index='Date', 
    values='Orders'
).fillna('').reset_index()
df.columns.name = None

# Display the final results
df
