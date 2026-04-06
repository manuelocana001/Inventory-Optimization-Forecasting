import pandas as pd
import sqlite3

# Create SQLite database
conn = sqlite3.connect('inventory.db')

# Load CSVs
sales_df = pd.read_csv('inventory_sales_data.csv')
sku_df = pd.read_csv('sku_master_data.csv')

# Write to SQLite
sales_df.to_sql('inventory_sales_data', conn, if_exists='replace', index=False)
sku_df.to_sql('sku_master_data', conn, if_exists='replace', index=False)

conn.close()

print("✅ Data loaded into inventory.db")
print(f"   - {len(sales_df)} sales records")
print(f"   - {len(sku_df)} SKUs")