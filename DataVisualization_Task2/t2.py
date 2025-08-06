# visualization.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Step 1: Load Dataset
# -----------------------------
try:
    data = pd.read_csv("Sample - Superstore.csv", encoding="latin1")
    print("✅ Dataset loaded successfully")
except:
    print("❌ Error loading dataset. Check the file path.")

# See first 5 rows
print(data.head())

# -----------------------------
# Step 2: Data Cleaning
# -----------------------------
print("\nChecking missing values:")
print(data.isnull().sum())

# Fill missing values (optional)
data = data.fillna("Unknown")

# -----------------------------
# Step 3: Visualization 1 - Sales by Category
# -----------------------------
plt.figure(figsize=(8,5))
sns.barplot(x="Category", y="Sales", data=data, estimator=sum, ci=None)
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.savefig("sales_by_category.png")
plt.show()

# -----------------------------
# Step 4: Visualization 2 - Sales by Region
# -----------------------------
plt.figure(figsize=(8,5))
sns.barplot(x="Region", y="Sales", data=data, estimator=sum, ci=None)
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.savefig("sales_by_region.png")
plt.show()

# -----------------------------
# Step 5: Visualization 3 - Profit vs Sales Scatter
# -----------------------------
plt.figure(figsize=(8,5))
sns.scatterplot(x="Sales", y="Profit", hue="Category", data=data)
plt.title("Profit vs Sales by Category")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.savefig("profit_vs_sales.png")
plt.show()

# -----------------------------
# Step 6: Visualization 4 - Top 10 States by Sales
# -----------------------------
top_states = data.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_states.index, y=top_states.values)
plt.title("Top 10 States by Sales")
plt.xticks(rotation=45)
plt.ylabel("Sales")
plt.savefig("top_states_sales.png")
plt.show()

# -----------------------------
# Step 7: Visualization 5 - Sales by Ship Mode (Pie Chart)
# -----------------------------
ship_mode_sales = data.groupby("Ship Mode")["Sales"].sum()
plt.figure(figsize=(6,6))
plt.pie(ship_mode_sales, labels=ship_mode_sales.index, autopct='%1.1f%%', startangle=140)
plt.title("Sales Distribution by Ship Mode")
plt.savefig("sales_by_shipmode.png")
plt.show()

# -----------------------------
# Step 8: Business Insights Summary
# -----------------------------
print("\n📊 Key Business Insights:")
print("1. Technology category generates the highest total sales.")
print("2. The West region contributes the maximum sales.")
print("3. Profit increases with sales in Technology, but some categories show losses at high sales.")
print("4. California and New York are the top sales-performing states.")
print("5. Standard Class is the most common shipping mode for sales.")

