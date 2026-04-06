# Inventory & Demand Forecasting Data Generator
# Creates 2 years of daily sales data for 200 SKUs with realistic demand patterns

import pandas as pd
import numpy as np 
from datetime import datetime, timedelta
import random

# Configuration
np.random.seed(42)
random.seed(42)

num_skus = 200
num_days = 730
start_date = datetime(2023, 1, 1)

# Generate SKU information
categories = ['Electronics', 'Apparel', 'Home & Garden', 'Food & Beverage', 'Health & Beauty']
skus = []

for i in range(num_skus):
    sku = {
        'SKU_ID': f'SKU-{i+1:04d}',
        'Product_Name': f'Product {i+1}',
        'Category': random.choice(categories),
        'Unit_Cost': round(random.uniform(5, 200), 2),
        'Lead_Time_Days': random.randint(7, 45)
    }
    skus.append(sku)

sku_df = pd.DataFrame(skus)
print(f"Generated {len(sku_df)} SKUs")

# Generate sales transactions
sales_data = []

for sku in skus:
    sku_id = sku['SKU_ID']
    base_demand = random.choice([50, 30, 15, 8, 3])
    variability = random.choice(['stable', 'moderate', 'erratic'])
    
    for day in range(num_days):
        date = start_date + timedelta(days=day)
        
        if variability == 'stable':
            daily_demand = int(np.random.normal(base_demand, base_demand * 0.1))
        elif variability == 'moderate':
            daily_demand = int(np.random.normal(base_demand, base_demand * 0.3))
        else:
            daily_demand = int(np.random.normal(base_demand, base_demand * 0.6))
        
        daily_demand = max(0, daily_demand)
        
        sales_data.append({
            'Date': date,
            'SKU_ID': sku_id,
            'Quantity_Sold': daily_demand
        })

print(f"Generated {len(sales_data)} sales records")

# Convert and save
sales_df = pd.DataFrame(sales_data)
sales_df.to_csv('inventory_sales_data.csv', index=False)
sku_df.to_csv('sku_master_data.csv', index=False)

print(f"\n✅ Files created successfully!")
print(f"   - inventory_sales_data.csv ({len(sales_df)} records)")
print(f"   - sku_master_data.csv ({len(sku_df)} SKUs)")