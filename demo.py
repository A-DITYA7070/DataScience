import pandas as pd

# Read the Excel file
df = pd.read_excel("compare.xlsx")

# Rename the columns
df.columns = ['A', 'B','result']

# Extract the columns 'A' and 'B'
col1 = list(df['A'])
col2 = list(df['B'])

l = list(set(col1) - set(col2))

df['new_result'] = pd.Series(l).reindex(df.index, fill_value='')
# Save the updated DataFrame back to the Excel file

df.to_excel("compare.xlsx", index=False)

print("added")




