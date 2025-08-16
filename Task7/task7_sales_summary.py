import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database (this will create sales_data.db if it doesn't exist)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Step 1: Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INT,
    price REAL
)
""")

# Step 2: Insert sample data if table is empty
cursor.execute("SELECT COUNT(*) FROM sales")
count = cursor.fetchone()[0]

if count == 0:
    cursor.executemany("""
    INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)
    """, [
        ("Laptop", 5, 60000),
        ("Laptop", 3, 60000),
        ("Phone", 10, 20000),
        ("Phone", 8, 20000),
        ("Headphones", 15, 2000),
        ("Headphones", 20, 2000),
        ("Tablet", 7, 25000),
        ("Tablet", 5, 25000),
    ])
    conn.commit()
    print("Sample data inserted ✅")

# Step 3: Run SQL query
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""
df = pd.read_sql_query(query, conn)

# Step 4: Print results
print("\nSales Summary:")
print(df)

# Step 5: Plot bar chart
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.title("Revenue by Product")
plt.ylabel("Revenue")
plt.xlabel("Product")
plt.tight_layout()
plt.show()

# Close connection
conn.close()
