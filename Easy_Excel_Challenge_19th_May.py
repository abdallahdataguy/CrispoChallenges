# Link to the challenge
# https://www.linkedin.com/posts/crispo-mwangi-6ab49453_excel-excelchallenges-india-activity-7197838405433511936-95uJ/

# This is "Python in Excel" script

# Read the Excel range
df = xl("B2:E11", headers=True)

# Perform data wrangling
df['Concat'] = df.apply(lambda x: ''.join(sorted(x[1:])), axis=1)
df['Unique'] = df['Concat'].map(lambda x: (df['Concat'] == x).sum() == 1)

# Display the output
df['Product'][df['Unique']]
