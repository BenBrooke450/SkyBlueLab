# Data Dictionary: Dairy-to-Cheddar Forecasting Pipeline

This data dictionary defines the unified features required to build a multi-stage forecasting model. The pipeline predicts milk yield at $T_0$ to satisfy aged cheddar demand at $T+6$ months.

---

### 1. Environmental Features (The Predictors)
*Used to calculate biological stress levels and pasture productivity.*

| Feature Name | Description | Units |
| :--- | :--- | :--- |
| `temp_hourly` | **Hourly Temperature** – Used to identify peak heat periods that stress cattle. | °C |
| `rh_hourly` | **Relative Humidity** – Critical for calculating moisture-driven heat stress. | % |
| `thi_index` | **Temperature Humidity Index (THI)** – Calculated as: $0.8 \times T + RH \times (T - 14.4) + 46.4$. | Index |
| `pasture_index` | **Pasture Quality Index** – Composite score based on rainfall and solar radiation from the preceding 90 days. | Score (0-1) |
| `region_id` | **Regional Location ID** – Categorical mapping connecting weather data to farm clusters. | ID |



---

### 2. Biological & Yield Features (The Ingredients)
*The chemical components that determine the physical conversion of milk to curd.*

| Feature Name | Description | Units |
| :--- | :--- | :--- |
| `milk_fat_pct` | **Milk Fat Content** – The primary solid-mass driver for Cheddar weight. | % |
| `casein_pct` | **Casein/Protein Content** – The structural "net" that determines curd efficiency. | % |
| `hist_yield_ratio`| **Historical Yield Ratio** – The actual recorded conversion rate ($kg \div liters$). | Ratio |

---

### 3. Supply Chain & Cost Features (The Constraints)
*Financial inputs used to optimize procurement volume vs. storage costs.*

| Feature Name | Description | Units |
| :--- | :--- | :--- |
| `milk_spot_price` | **Raw Milk Spot Price** – The cost per liter at the time of procurement ($T_0$). | €/Liter |
| `utility_rate` | **Refrigeration Utility Rates** – Energy cost to maintain aging rooms at $4–7^\circ C$. | €/kWh |
| `shrinkage_rate` | **Moisture Loss Rate** – Predicted percentage of weight lost during 6-month aging. | % |
| `stockout_penalty`| **Stockout Penalty Cost** – Financial penalty per kg for failing to meet retail SLAs. | €/kg |
| `disposal_cost` | **Wastage Cost** – Cost per kg if cheese fails quality checks or expires. | €/kg |



---

### 4. Market & Demand Features (The Targets)
*Forward-looking data points used to define the production goal.*

| Feature Name | Description | Units |
| :--- | :--- | :--- |
| `hist_sales_vol` | **Historical Weekly Sales** – Volume sold in the same window in previous years. | kg |
| `target_vol` | **Target Retail Volume** – The specific quantity required by the retail partner at $T+6$. | kg |
| `promo_flag` | **Promotional Flag** – Binary indicator (0/1) for scheduled marketing campaigns. | Boolean |
| `competitor_idx` | **Competitor Pricing Index** – Forecasted pricing of rival premium brands. | Index |
| `wholesale_fcst` | **Wholesale Price Forecast** – The expected price the retailer will pay in 6 months. | €/kg |