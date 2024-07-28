# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/crispo-mwangi-6ab49453_excelchallenge-excel-crispexcel-activity-7223198077187198976-LXd4/

# Read the data range
df = xl("B3:D11", headers=True)

# Perform data munging
df['ind'] = (df['Student'] != df['Student'].shift(1)).cumsum()
df = df.pivot(
    index=['ind', 'Student'], columns='Test', values='Result'
).reset_index().fillna('exempt')
df = df.iloc[:, 1:]
df.columns = [''] + df.columns[1:].tolist()

# Display the final results
df
