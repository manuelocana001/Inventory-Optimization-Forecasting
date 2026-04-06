-- Reorder Point and Safety Stock Calculator
-- SQLite-compatible version using variance calculation

WITH sku_demand_stats AS (
    SELECT 
        s.SKU_ID,
        AVG(s.Quantity_Sold) as Avg_Daily_Demand,
        -- Calculate std dev manually: sqrt(avg(x^2) - avg(x)^2)
        SQRT(AVG(s.Quantity_Sold * s.Quantity_Sold) - AVG(s.Quantity_Sold) * AVG(s.Quantity_Sold)) as Std_Daily_Demand,
        COUNT(*) as Days_of_Data
    FROM inventory_sales_data s
    GROUP BY s.SKU_ID
),
reorder_calculations AS (
    SELECT 
        m.SKU_ID,
        m.Product_Name,
        m.Category,
        m.Lead_Time_Days,
        d.Avg_Daily_Demand,
        d.Std_Daily_Demand,
        -- Safety Stock (Z=1.65 for 95% service level)
        ROUND(1.65 * d.Std_Daily_Demand * SQRT(m.Lead_Time_Days), 0) as Safety_Stock,
        -- Reorder Point
        ROUND((d.Avg_Daily_Demand * m.Lead_Time_Days) + 
              (1.65 * d.Std_Daily_Demand * SQRT(m.Lead_Time_Days)), 0) as Reorder_Point
    FROM sku_master_data m
    JOIN sku_demand_stats d ON m.SKU_ID = d.SKU_ID
)
SELECT 
    SKU_ID,
    Product_Name,
    Category,
    Lead_Time_Days,
    ROUND(Avg_Daily_Demand, 2) as Avg_Daily_Demand,
    Safety_Stock,
    Reorder_Point
FROM reorder_calculations
ORDER BY Reorder_Point DESC;