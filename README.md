### 📌 **Project Objective**

This project analyzes **12 months of retail sales data** using Python and Pandas to identify:

* Monthly revenue trends
* Peak order days
* City-wise performance
* Most sold products
* Product combinations bought together

---

### 📂 **Data Source**

* Folder: `SalesData/`
* Files: 12 CSVs (one for each month)
* Final merged file: `Sales.csv`

---

### 🧹 **1. Data Cleaning and Preparation**

* Merged 12 monthly files using `os` and `pandas.concat()`
* Dropped rows with missing values
* Removed header rows mistakenly included in data
* Converted data types:

  * `Quantity Ordered` → integer
  * `Price Each` → float
  * `Order Date` → datetime format
* Added new columns:

  * `amount` = Quantity × Price
  * `City` = extracted from `Purchase Address`
  * `month`, `month name`, `day name`

---

### 📈 **2. Monthly Sales Analysis**

* Grouped data by month
* Calculated:

  * Total revenue per month
  * Average sales per month
* Saved analysis to `Analysis/MontlySales.csv`
* Visualized using `matplotlib` → `MonthlySales.png`

---

### 📊 **3. Orders by Day of the Week**

* Counted number of orders on each weekday
* Saved to `Ordersbyday.csv`
* Visualized as bar chart → `Ordersbyday.png`
* Also tagged weekends using `IsHoliday` column

---

### 🏙️ **4. City-Wise Analysis**

* Grouped by city to find:

  * Total orders
  * Quantity sold
  * Total revenue
* Saved to `City.csv`
* Visualized → `City.png` (Grouped bar chart for each city)

---

### 🤝 **5. Frequently Bought Together (Product Bundles)**

* Found duplicate `Order ID`s (multiple products in same order)
* Combined product names in each group
* Saved to `duplicate.csv`
* Used `itertools.combinations()` + `Counter` to find:

  * Most common product pairs bought together

---

### 📦 **Libraries Used**

* `pandas`
* `numpy`
* `matplotlib`
* `itertools`
* `os`
* `collections.Counter`

---

### 📁 **Folder Structure**

```
Retail-Sales-Analysis/
│
├── SalesData/              → Raw 12-month CSVs
├── Analysis/               → Processed data + Charts
│   ├── MontlySales.csv
│   ├── Ordersbyday.csv
│   ├── City.csv
│   ├── duplicate.csv
│   ├── MonthlySales.png
│   ├── Ordersbyday.png
│   └── City.png
├── Sales.csv               → Merged full data
├── Retail_Sales_Analysis.py → Python project code
└── README.md               → Project summary
```

---

### ✅ **Key Insights**

* Highest sales were recorded in **December**
* Most orders are placed on **Monday**
* **San Francisco** generated the most revenue
* **Phones & Chargers** are often bought together

---

### 🔗 **GitHub Link**

### 🔗 **GitHub Link**  
[https://github.com/pratimachauhan/Retail-Sales-Analysis](https://github.com/pratimachauhan/Retail-Sales-Analysis)


---


