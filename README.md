# Sales Data Analysis Project

## Overview
This project focuses on analyzing sales data using Python, Pandas, and Matplotlib. The dataset contains details of product sales, including date, product name, units sold, revenue, and category. The analysis includes data preprocessing, exploratory data analysis, visualization, and revenue growth rate calculations.

## Dataset Structure
The dataset (`sales_data.csv`) contains the following columns:
- **Date**: Date of the sale (YYYY-MM-DD format).
- **Product**: Product name (e.g., "Laptop", "Mobile", "Headphones").
- **Units Sold**: The number of units sold.
- **Revenue**: The total revenue from the sale.
- **Category**: The category of the product (e.g., "Electronics", "Accessories").

## Data Preprocessing
The dataset is cleaned and processed as follows:
- Loaded into a Pandas DataFrame.
- Checked for missing values and handled them appropriately (dropped or filled).
- Ensured the `Date` column is in the correct datetime format.
- Removed rows where `Units Sold` or `Revenue` is negative.

## Data Analysis
The analysis includes:
- Calculating the total revenue for each product using `groupby`.
- Computing the average units sold per product.
- Identifying the product with the highest revenue and highest units sold.

## Data Visualization
Using Matplotlib, the following visualizations are generated:
- **Bar Chart**: Displays the total revenue by product.
- **Line Plot**: Shows the trend of revenue over time.
- **Pie Chart**: Illustrates the distribution of revenue across different product categories.

## Bonus Calculation
- Calculates the revenue growth rate for each product by comparing total revenue in the first and last month of data.
- Identifies the product(s) with the highest growth rate.

## Technologies Used
- **Python**: For data processing and analysis.
- **Pandas**: For data manipulation.
- **Matplotlib**: For data visualization.
- **CSV**: Data storage and handling.

## 🚀 How to Run the Project

### 1️⃣ Install & Setup Python
- Download and install [Python](https://www.python.org/downloads/).
- Ensure `pip` is installed and updated.
- Install the required dependencies:
  ```sh
  pip install pandas matplotlib
  ```

### 2️⃣ Load the Dataset
- Place the `sales_data.csv` file in the project directory.
- Ensure the file is formatted correctly.

### 3️⃣ Run the Analysis
- Navigate to the project folder:
  ```sh
  cd sales-data-analysis
  ```
- Execute the script:
  ```sh
  python analysis.py
  ```

### 4️⃣ View Results
- The script will display key insights and generate visualizations.
- Review the plots and summary statistics in the output.

## Author
This project was developed for data analysis and visualization practice.

## License
This project is open-source and available under the MIT License.

---

## GitHub README.md
To add this file to your GitHub repository:
1. Save this file as `README.md` in the root of your project directory.
2. Navigate to your project folder in the terminal and run the following commands:
   ```sh
   git add README.md
   git commit -m "Added project README"
   git push origin main
   ```

