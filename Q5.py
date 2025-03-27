import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file into a DataFrame
file_name = "sales_data.csv"

try:
    df = pd.read_csv(file_name)
    print("First few rows of the dataset:")
    print(df.head())
except FileNotFoundError:
    print(f"File '{file_name}' not found. Please ensure it exists in the current directory.")
    exit()

# Step 2: Check for missing values and handle them
print("\nChecking for missing values:")
print(df.isnull().sum())

# Fill missing values with appropriate defaults or drop rows
df.fillna({'Category': 'Unknown', 'Units Sold': 0, 'Revenue': 0}, inplace=True)

# Step 3: Ensure 'Date' column is in datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop rows with invalid dates
df = df.dropna(subset=['Date'])

# Step 4: Remove rows with negative 'Units Sold' or 'Revenue'
df = df[(df['Units Sold'] >= 0) & (df['Revenue'] >= 0)]

# Step 5: Data Analysis
# Total revenue by product
total_revenue = df.groupby('Product')['Revenue'].sum()
print("\nTotal Revenue by Product:")
print(total_revenue)

# Average units sold per product
average_units_sold = df.groupby('Product')['Units Sold'].mean()
print("\nAverage Units Sold per Product:")
print(average_units_sold)

# Product with highest revenue and highest units sold
highest_revenue_product = total_revenue.idxmax()
highest_units_sold_product = df.groupby('Product')['Units Sold'].sum().idxmax()
print(f"\nProduct with highest revenue: {highest_revenue_product}")
print(f"Product with highest units sold: {highest_units_sold_product}")

# Step 6: Data Visualization
# Bar chart showing total revenue by product
total_revenue.plot(kind='bar', figsize=(10, 6), color='skyblue', title='Total Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.tight_layout()
plt.show()

# Line plot showing revenue trend over time
revenue_trend = df.groupby('Date')['Revenue'].sum()
revenue_trend.plot(kind='line', figsize=(10, 6), title='Revenue Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.tight_layout()
plt.show()

# Pie chart showing revenue distribution across categories
category_revenue = df.groupby('Category')['Revenue'].sum()
category_revenue.plot(kind='pie', figsize=(8, 8), autopct='%1.1f%%', title='Revenue Distribution by Category')
plt.ylabel('')
plt.tight_layout()
plt.show()

# Bonus Calculation: Growth rate of revenue for each product
df['Month'] = df['Date'].dt.to_period('M')
monthly_revenue = df.groupby(['Product', 'Month'])['Revenue'].sum().unstack()
growth_rate = (monthly_revenue.iloc[:, -1] - monthly_revenue.iloc[:, 0]) / monthly_revenue.iloc[:, 0] * 100

print("\nGrowth rate of revenue for each product:")
print(growth_rate)

highest_growth_product = growth_rate.idxmax()
print(f"\nProduct with highest growth rate: {highest_growth_product} ({growth_rate[highest_growth_product]:.2f}%)")
