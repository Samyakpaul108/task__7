import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# Create sales table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL,
    date TEXT
)
''')

# Insert sample data
sample_data = [
    ('Laptop', 5, 999.99, '2024-01-01'),
    ('Smartphone', 10, 699.99, '2024-01-01'),
    ('Tablet', 8, 499.99, '2024-01-02'),
    ('Laptop', 3, 999.99, '2024-01-02'),
    ('Smartphone', 7, 699.99, '2024-01-03'),
    ('Tablet', 4, 499.99, '2024-01-03')
]

cursor.executemany('''
INSERT OR IGNORE INTO sales (product, quantity, price, date)
VALUES (?, ?, ?, ?)
''', sample_data)

# Commit the changes
conn.commit()

# Query 1: Get total quantity and revenue by product
query1 = """
SELECT 
    product,
    SUM(quantity) AS total_quantity,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product
"""

# Query 2: Daily sales analysis
query2 = """
SELECT 
    date,
    SUM(quantity) AS daily_quantity,
    SUM(quantity * price) AS daily_revenue
FROM sales
GROUP BY date
ORDER BY date
"""

# Query 3: Product price distribution
query3 = """
SELECT 
    product,
    price,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY product, price
"""

# Execute queries and load into pandas DataFrames
df1 = pd.read_sql_query(query1, conn)
df2 = pd.read_sql_query(query2, conn)
df3 = pd.read_sql_query(query3, conn)

# Display the results
print("\nSales Summary by Product:")
print("=" * 40)
print(df1.to_string(index=False))
print("\n")

print("\nDaily Sales Analysis:")
print("=" * 40)
print(df2.to_string(index=False))
print("\n")

print("\nProduct Price Distribution:")
print("=" * 40)
print(df3.to_string(index=False))
print("\n")

# Create figures for all visualizations
plt.figure(figsize=(15, 10))

# Plot 1: Revenue by Product
plt.subplot(2, 2, 1)
df1.plot(kind='bar', x='product', y='total_revenue', color='skyblue', ax=plt.gca())
plt.title('Total Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)

# Plot 2: Daily Revenue Trend
plt.subplot(2, 2, 2)
df2.plot(kind='line', x='date', y='daily_revenue', marker='o', color='green', ax=plt.gca())
plt.title('Daily Revenue Trend')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)

# Plot 3: Quantity Distribution by Product
plt.subplot(2, 2, 3)
df3.plot(kind='bar', x='product', y='total_quantity', color='orange', ax=plt.gca())
plt.title('Quantity Distribution by Product')
plt.xlabel('Product')
plt.ylabel('Total Quantity')
plt.xticks(rotation=45)

# Plot 4: Price Distribution
plt.subplot(2, 2, 4)
df3.plot(kind='scatter', x='product', y='price', s=df3['total_quantity']*50, color='red', ax=plt.gca())
plt.title('Price Distribution with Quantity Size')
plt.xlabel('Product')
plt.ylabel('Price ($)')
plt.xticks(rotation=45)

# Adjust layout and save the chart
plt.tight_layout()
plt.savefig('sales_analysis.png')
print("All charts saved as 'sales_analysis.png'")

# Close the database connection
conn.close() 