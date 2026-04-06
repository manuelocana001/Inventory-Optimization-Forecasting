# Inventory-Optimization-Forecasting
ABC-XYZ inventory classification and demand forecasting analysis using Python, SQL, and Tableau.
# Inventory Optimization & Demand Forecasting

## 📊 Project Overview

Analyzed 2 years of daily sales data (146,000 transactions across 200 SKUs) to solve a retail distributor's dual problem: overstock on slow-movers wasting cash and frequent stockouts on bestsellers losing sales. Built end-to-end solution using ABC-XYZ classification, demand forecasting, and data-driven reorder point recommendations.

## 🔍 Business Problem

The company faced:
- **Cash tied up in dead inventory** — Low-value, erratic SKUs consuming warehouse space
- **Lost revenue from stockouts** — High-demand items running out before replenishment
- **No data-driven restocking strategy** — Reorder decisions based on gut feel, not analytics

## 💡 Solution & Key Findings

### ABC-XYZ Inventory Segmentation
Classified all 200 SKUs into 9 categories based on revenue contribution and demand variability:

- **53 SKUs (26.5%) generate 69.5% of revenue** — Classic Pareto principle validated
- **38 AX items (High-value, Stable)** — Top priority for forecasting and inventory management
- **15 AY items (High-value, Moderate variability)** — Require additional safety stock
- **96 C-category items** — Low-value SKUs; candidates for SKU rationalization

**Strategic Insight:** Focus forecasting resources on the 53 A-category SKUs. The 96 C-category items should be reviewed quarterly for potential discontinuation.

### Reorder Point Optimization
Calculated optimal reorder points using statistical formulas:
- **Formula:** Reorder Point = (Avg Daily Demand × Lead Time) + Safety Stock
- **Safety Stock:** Z-score (1.65 for 95% service level) × Std Demand × √Lead Time
- **Example:** SKU-0182 (top-selling item) has reorder point of 2,523 units based on 50-unit daily demand

**Impact:** Eliminates guesswork from restocking decisions; prevents both stockouts and overstock.

### Demand Variability Analysis
- **130 SKUs classified as X (Stable)** — Predictable demand patterns, easy to forecast
- **70 SKUs classified as Y (Moderate)** — Require buffer stock due to variability
- **0 Z (Erratic) items** — Data showed no extreme demand volatility

## 🛠️ Technical Implementation

### Tools & Technologies
- **Python** (pandas, numpy) — Data generation, EDA, ABC-XYZ classification
- **SQL** (SQLite) — Reorder point calculations, safety stock formulas
- **Tableau** — Interactive dashboard with classification matrix and trend analysis

### Data Pipeline
1. **Data Generation** — Created synthetic but realistic dataset: 200 SKUs × 730 days
2. **Python Analysis** — Calculated revenue contribution, demand variability (Coefficient of Variation)
3. **SQL Calculations** — Implemented reorder point and safety stock formulas
4. **Visualization** — Built 3-chart Tableau dashboard showing classification, top SKUs, and trends

### Key Metrics Calculated
- Total revenue per SKU
- Average daily demand
- Standard deviation of demand
- Coefficient of Variation (CV = σ/μ)
- Safety stock (95% service level)
- Reorder points by SKU

## 📈 Deliverables

### [View Live Tableau Dashboard](https://public.tableau.com/app/profile/manuel.ramirez3002/viz/InventoryOptimizationDashboard_17754907143180/Dashboard1)

**Dashboard Features:**
- ABC-XYZ classification heatmap showing SKU distribution
- Top 10 SKUs by revenue
- Demand trend analysis over 24 months

### Project Files
- `generate_inventory_data.py` — Synthetic dataset generator
- `inventory_analysis.py` — ABC-XYZ classification logic
- `reorder_point_calculator.sql` — Reorder point and safety stock calculations
- `inventory_sales_data.csv` — 146,000 sales transactions
- `sku_master_data.csv` — 200 SKU master list
- `sku_abc_xyz_classification.csv` — Classification results

## 🎯 Skills Demonstrated

**Inventory Management:**
- ABC-XYZ analysis and segmentation
- Safety stock and reorder point formulas
- Demand variability measurement (Coefficient of Variation)
- Service level optimization (95% target)

**Technical Skills:**
- Python data analysis (pandas aggregations, groupby operations)
- SQL statistical calculations (variance, standard deviation workarounds)
- Time series data manipulation
- Data visualization and dashboard design

**Business Analysis:**
- Identifying Pareto principle in action (80/20 rule)
- Translating statistical outputs into business recommendations
- SKU rationalization strategy
- Risk-based inventory prioritization

## 📊 Business Impact

**Quantified Recommendations:**
- **Focus forecasting on 53 A-category SKUs** — Generates 70% of revenue with only 26% of SKU count
- **Implement calculated reorder points** — Eliminates reactive "panic ordering" and reduces stockout risk
- **Review 96 C-category items** — Low revenue contribution; potential to free up warehouse space and reduce carrying costs
- **Maintain 95% service level** — Balanced approach prevents both stockouts and excessive safety stock

---

**Built as part of a supply chain analytics portfolio demonstrating end-to-end problem-solving from data generation through actionable business insights.**
