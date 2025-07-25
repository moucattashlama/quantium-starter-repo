import pandas as pd
import glob

# Step 1: Find all CSV files in the folder
file_paths = glob.glob("*.csv")
print("Found files:", file_paths)

# Step 2: Merge all files
dfs = [pd.read_csv(file) for file in file_paths]
merged_df = pd.concat(dfs, ignore_index=True)

# ✅ Step 3: Filter only pink morsel sales
merged_df = merged_df[merged_df['product'] == 'pink morsel'].copy()

# Step 4: Clean and convert 'price' column
merged_df['price'] = merged_df['price'].replace(r'[\$,]', '', regex=True).astype(float)

# Step 5: Compute 'Sales' = price * quantity
merged_df['Sales'] = merged_df['price'] * merged_df['quantity']

# Step 6: Convert 'date' column to datetime
merged_df['Date'] = pd.to_datetime(merged_df['date'])

# Step 7: Select only required columns
final_df = merged_df[['Sales', 'Date', 'region']].rename(columns={'region': 'Region'})

# Step 8: Save to CSV
final_df.to_csv("formatted_data.csv", index=False)

print("✅ Filtered and cleaned file saved as 'formatted_data.csv' with: Sales, Date, Region")
