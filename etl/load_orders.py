import pandas as pd

# 1. Daten laden
df = pd.read_csv("data/raw/olist_orders_dataset.csv")

# 2. Überblick
print("Original shape:", df.shape)
print(df.isnull().sum())

# 3. Duplikate entfernen
df = df.drop_duplicates()

# 4. Datums-Spalten korrekt umwandeln
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    df[column] = pd.to_datetime(df[column], errors="coerce")

# 5. Bereinigte Daten speichern
df.to_csv("data/processed/orders_clean.csv", index=False)

print("Cleaned shape:", df.shape)
print("Saved to data/processed/orders_clean.csv")