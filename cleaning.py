import pandas as pd
import glob

# Find all CSVs in the same folder
file_paths = glob.glob("*.csv")
print("Found files:", file_paths)

# Merge them
dfs = [pd.read_csv(file) for file in file_paths]
merged_df = pd.concat(dfs, ignore_index=True)

# Save the merged output in the same folder
merged_df.to_csv("merged_data.csv", index=False)

print("✅ CSV files merged successfully into 'merged_data.csv'")
