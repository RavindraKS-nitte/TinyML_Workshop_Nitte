import pandas as pd

# Load the dataset
df = pd.read_csv("../Datasets/dataset.csv")

# remove duplicate rows
duplicate_count = df.duplicated().sum()
print("Duplicate Rows:",duplicate_count)

#remove duplicates
df = df.drop_duplicates()

#verify datset
print("New Shape:",df.shape)