# 🛒 Retail Sales Analysis

This project analyzes 12 months of retail sales data to uncover business insights such as monthly revenue trends, popular products, city-wise performance, and frequently bought product combinations.

---

## 📁 Project Structure

Retail-Sales-Analysis/  
├── SalesData/               # Contains 12 months raw CSV files  
├── Analysis/                # Output visualizations and CSVs  
├── Sales.csv                # Combined cleaned dataset  
├── main.py                  # All code for data cleaning & analysis  
├── requirements.txt         # Required Python libraries  
└── README.md                # Project documentation  

---

## 🧠 Key Insights

- 📆 **Monthly Revenue**: Visual trend of total monthly sales.  
- 📅 **Orders by Day**: Find which day has the most orders.  
- 🏙️ **Top Performing City**: Most orders, quantity, and revenue.  
- 💼 **Holiday Impact**: Sales comparison on weekends vs weekdays.  
- 🛍️ **Product Pairs**: Products frequently bought together.  

---

## 📊 Visual Output Samples

### 1. Monthly Sales Trend  
![Monthly Sales](Analysis/MonthlySales.png)

### 2. Orders by Day  
![Orders by Day](Analysis/Ordersbyday.png)

### 3. City-wise Order Analysis  
![City Analysis](Analysis/City.png)

---

## ▶️ How to Run This Project

1. Clone the repository:  
   ```bash
   git clone https://github.com/PratimaChauhan1207/Retail-Sales-Analysis.git
   cd Retail-Sales-Analysis
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:

   ```bash
   python main.py
   ```

---

## 🛠 Libraries Used

* pandas
* matplotlib
* numpy
* os
* datetime
* collections.Counter

---

## 📦 Dataset

12 individual CSV files for each month placed inside the `/SalesData` folder. These files are merged into a single `Sales.csv` for processing.

---

## 🔗 GitHub Link

[https://github.com/PratimaChauhan1207/Retail-Sales-Analysis](https://github.com/PratimaChauhan1207/Retail-Sales-Analysis)

---

## 🙋‍♀️ About Me

Pratima Chauhan
Aspiring Data Analyst | Learning Python, Pandas, Power BI | Focused on turning data into stories.
📫 Reach me on LinkedIn

---

## 🔧 Extra Suggestion

Add a `requirements.txt` file with:

```
pandas
numpy
matplotlib
```


