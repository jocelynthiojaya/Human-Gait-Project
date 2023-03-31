import pandas as pd

folder = "temp"

df = pd.read_csv(folder + "/filename.csv")

# Using DataFrame.insert() to add a column
df.insert(0, "id", "1", True)

print(df.head())

df.to_csv(folder + '/filename.csv', index=False)