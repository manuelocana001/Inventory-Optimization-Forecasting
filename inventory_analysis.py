# Inventory Analysis - ABC-XYZ Classification
# Analyzes 2 years of sales data to classify SKUs by revenue and variability

import pandas as pd
import numpy as np

# Load data
sales_df = pd.read_csv('inventory_sales_data.csv')
sku_df = pd.read_csv('sku_master_data.csv')

print(f"Loaded {len(sales_df)} sales records")
print(f"Loaded {len(sku_df)} SKUs")

# Merge sales with SKU master to get unit costs
sales_with_cost = sales_df.merge(sku_df[['SKU_ID', 'Unit_Cost']], on='SKU_ID')

# Calculate revenue per transaction
sales_with_cost['Revenue'] = sales_with_cost['Quantity_Sold'] * sales_with_cost['Unit_Cost']

# Aggregate by SKU
sku_metrics = sales_with_cost.groupby('SKU_ID').agg({
    'Quantity_Sold': ['sum', 'mean', 'std'],
    'Revenue': 'sum'
}).reset_index()

# Flatten column names
sku_metrics.columns = ['SKU_ID', 'Total_Qty_Sold', 'Avg_Daily_Demand', 'Std_Daily_Demand', 'Total_Revenue']

print("\nSKU Metrics calculated:")
print(sku_metrics.head())

# Sort by revenue descending
sku_metrics = sku_metrics.sort_values('Total_Revenue', ascending=False).reset_index(drop=True)

# Calculate cumulative revenue percentage
sku_metrics['Cumulative_Revenue'] = sku_metrics['Total_Revenue'].cumsum()
total_revenue = sku_metrics['Total_Revenue'].sum()
sku_metrics['Cumulative_Pct'] = (sku_metrics['Cumulative_Revenue'] / total_revenue) * 100

# Assign ABC category
def assign_abc(cumulative_pct):
    if cumulative_pct <= 70:
        return 'A'
    elif cumulative_pct <= 90:
        return 'B'
    else:
        return 'C'

sku_metrics['ABC_Category'] = sku_metrics['Cumulative_Pct'].apply(assign_abc)

print("\nABC Classification:")
print(sku_metrics['ABC_Category'].value_counts().sort_index())

# Calculate coefficient of variation (CV = std / mean)
sku_metrics['Coefficient_of_Variation'] = sku_metrics['Std_Daily_Demand'] / sku_metrics['Avg_Daily_Demand']

# Assign XYZ category based on CV
def assign_xyz(cv):
    if cv < 0.5:
        return 'X'  # Stable demand
    elif cv < 1.0:
        return 'Y'  # Moderate variability
    else:
        return 'Z'  # Erratic demand

sku_metrics['XYZ_Category'] = sku_metrics['Coefficient_of_Variation'].apply(assign_xyz)

# Combine ABC and XYZ
sku_metrics['ABC_XYZ'] = sku_metrics['ABC_Category'] + sku_metrics['XYZ_Category']

print("\nXYZ Classification:")
print(sku_metrics['XYZ_Category'].value_counts().sort_index())

print("\nABC-XYZ Matrix:")
print(pd.crosstab(sku_metrics['ABC_Category'], sku_metrics['XYZ_Category']))

# Merge back with SKU master data
final_results = sku_metrics.merge(sku_df[['SKU_ID', 'Product_Name', 'Category', 'Lead_Time_Days']], on='SKU_ID')

# Save to CSV
final_results.to_csv('sku_abc_xyz_classification.csv', index=False)

print("\n" + "="*60)
print("KEY INSIGHTS:")
print("="*60)

# High-priority SKUs (A category)
high_priority = final_results[final_results['ABC_Category'] == 'A']
print(f"\n📊 High-Value SKUs (A): {len(high_priority)} SKUs generating {high_priority['Total_Revenue'].sum()/total_revenue*100:.1f}% of revenue")

# Most stable high-value (AX)
ax_skus = final_results[final_results['ABC_XYZ'] == 'AX']
print(f"   - AX (High value, Stable): {len(ax_skus)} SKUs - Easy to forecast, high priority")

# Erratic high-value (AZ)
az_skus = final_results[final_results['ABC_XYZ'] == 'AZ']
print(f"   - AZ (High value, Erratic): {len(az_skus)} SKUs - Need safety stock!")

# Low-value erratic (CZ)
cz_skus = final_results[final_results['ABC_XYZ'] == 'CZ']
print(f"\n🗑️  Low-Value Erratic (CZ): {len(cz_skus)} SKUs - Consider discontinuing")

print(f"\n✅ Results saved to: sku_abc_xyz_classification.csv")

