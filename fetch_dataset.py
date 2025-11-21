import kagglehub
import pandas as pd
import os

path = kagglehub.dataset_download("nadyinky/sephora-products-and-skincare-reviews")

print("Path to dataset files:", path)

# Step 2: Find CSV files inside the dataset folder
csv_files = [f for f in os.listdir(path) if f.endswith(".csv")]

print("CSV files found:", csv_files)

# Step 3: Load a specific CSV file
df_product_info = pd.read_csv(os.path.join(path, csv_files[0]))
df_review = pd.read_csv(os.path.join(path, csv_files[1]))

print(df_product_info.head())
print(df_review["review_text"])