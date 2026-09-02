import pandas as pd
import os

files = os.listdir("data/raw")
print(files)

tables = {
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "customers": "olist_customers_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "reviews": "olist_order_reviews_dataset.csv",
    "geolocation": "olist_geolocation_dataset.csv",
    "category_translation": "product_category_name_translation.csv",
}

dfs = {}
for name, filename in tables.items():
    path = f"data/raw/{filename}"
    df = pd.read_csv(path)
    dfs[name] = df
    print(f"\n=== {name} ===")
    print("shape:", df.shape)
    print("columns:", list(df.columns))
    print("nulls:\n", df.isnull().sum()[df.isnull().sum() > 0])
    print("duplicate rows:", df.duplicated().sum())

    print(dfs["orders"]["order_status"].value_counts())