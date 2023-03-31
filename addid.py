import pandas as pd

folder = "temp"

df = pd.read_csv(folder + "/11_Philipwalk.csv")
#print(df.head())

# Using DataFrame.insert() to add a column
df.insert(0, "id", "11", True)
#df.insert(8, "age", ">40", True)

print(df.head())

df.to_csv(folder + '/11_Philipwalk.csv', index=False)