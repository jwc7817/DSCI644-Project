import pandas as pd

# load csv
df = pd.read_csv("data/fdic/fdic_data_full.csv")

# ensure last_updated col is datetime
df['last_updated'] = pd.to_datetime(df['last_updated'])

# sort descending for last_updated; most recent first
df_sorted = df.sort_values(by='last_updated', ascending=False)

# set row counts (split data into three categores due to API limit vagueness)
row_counts = [250, 500, 1000]
output_files = ["data/fdic/fdic_250.csv", "data/fdic/fdic_500.csv", "data/fdic/fdic_1000.csv"]

# export csvs
for count, filename in zip(row_counts, output_files):
    df_sorted.head(count).to_csv(filename, index=False)

print("csv files created!")