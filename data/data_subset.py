import pandas as pd

# load csv
# df = pd.read_csv("data/fdic/fdic_data_full.csv")
df = pd.read_csv("/data/iowa_liquor/iowa_big_datasets/iowa_liquor_sales_full.csv")

# ensure last_updated col is datetime
# df["last_updated"] = pd.to_datetime(df["last_updated"])  # for FDIC dataset
df["Date"] = pd.to_datetime(df["Date"])  # for Iowa liquor sales

# sort descending for last_updated; most recent first
# df_sorted = df.sort_values(by='last_updated', ascending=False)  # FDIC dataset
df_sorted = df.sort_values(by='Date', ascending=False)  # Iowa liquor sales

# set row counts (split data into three categores due to API limit vagueness)
row_counts = [250, 500, 1000]
# output_files = ["data/fdic/fdic_250.csv", "data/fdic/fdic_500.csv", "data/fdic/fdic_1000.csv"]
output_files = [
    "/Users/limey/school/2026-spring/DSCI 644/DSCI644-Project/data/iowa_liquor/iowa_liquor_250.csv",
    "/Users/limey/school/2026-spring/DSCI 644/DSCI644-Project/data/iowa_liquor/iowa_liquor_500.csv",
    "/Users/limey/school/2026-spring/DSCI 644/DSCI644-Project/data/iowa_liquor/iowa_liquor_1000.csv"
]
# export csvs
for count, filename in zip(row_counts, output_files):
    df_sorted.head(count).to_csv(filename, index=False)

print("csv files created!")