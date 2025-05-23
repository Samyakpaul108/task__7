Sales Analysis with SQLite and Python
Author: Samyak Paul

📊 Project Description
This project demonstrates a comprehensive sales data analysis system using Python, SQLite, and data visualization tools. It provides insights into sales performance through multiple analytical perspectives and visual representations.

🎯 Key Features
Database Management: Creates and manages a SQLite database for sales data
Data Analysis: Performs multiple analytical queries on sales data
Visualization: Generates multiple interactive charts and graphs
Comprehensive Reporting: Provides detailed sales summaries and trends
📈 Analysis Capabilities
Product Performance Analysis

Total quantity sold per product
Revenue generated by each product
Product-wise sales distribution
Temporal Analysis

Daily sales trends
Revenue patterns over time
Sales volume analysis by date
Price Analysis

Product price distribution
Quantity-weighted price analysis
Revenue contribution by price point
🛠 Technical Stack
Programming Language: Python 3.x
Database: SQLite3
Data Analysis: pandas
Visualization: matplotlib
Version Control: Git
📋 Requirements
Python 3.x
Required Python packages:
sqlite3 (built-in)
pandas
matplotlib
🚀 How to Run
Install required packages:
pip install pandas matplotlib
Run the Python script:
python sales_analysis.py
📊 Output
The script generates:

Detailed sales summary tables
Multiple visualization charts:
Product revenue bar chart
Daily revenue trend line chart
Quantity distribution bar chart
Price distribution scatter plot
All visualizations are saved in 'sales_analysis.png'
📚 SQL Queries
Product Performance Query:
SELECT 
    product,
    SUM(quantity) AS total_quantity,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product
Daily Sales Analysis:
SELECT 
    date,
    SUM(quantity) AS daily_quantity,
    SUM(quantity * price) AS daily_revenue
FROM sales
GROUP BY date
ORDER BY date
Price Distribution Analysis:
SELECT 
    product,
    price,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY product, price
🎓 Learning Outcomes
This project demonstrates:

SQLite database operations
SQL query writing and optimization
Data analysis using pandas
Data visualization with matplotlib
Python database connectivity
Data aggregation and reporting
Time series analysis
Price distribution analysis
📝 License
This project is open source and available under the MIT License.

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
