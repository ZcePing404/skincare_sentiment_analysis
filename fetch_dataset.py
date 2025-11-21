import kagglehub
import pandas as pd
import os

def load_dataset():
    path = kagglehub.dataset_download("nadyinky/sephora-products-and-skincare-reviews")

    csv_files = sorted([f for f in os.listdir(path) if f.endswith(".csv")])
    
    df_product_info = pd.read_csv(os.path.join(path, csv_files[0]))

    review_dfs = []
    for i in range(1, 6):
        review_path = os.path.join(path, csv_files[i])
        review_dfs.append(pd.read_csv(review_path))

    df_all_reviews = pd.concat(review_dfs, ignore_index=True)

    return df_product_info, df_all_reviews