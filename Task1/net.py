import pandas as pd

# Load the dataset (change path if needed)
df = pd.read_csv(r"C:\Users\rohit\OneDrive\Desktop\elevate labs\task1\archive\netflix_titles.csv")

# -----------------------------
# 1. Basic Exploration
# -----------------------------
print("Dataset Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nMissing Values:\n", df.isnull().sum())
print("\nData Types:\n", df.dtypes)

# -----------------------------
# 2. Handle Missing Values
# -----------------------------
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Not Available")
df['country'] = df['country'].fillna("Unknown")
df['date_added'] = df['date_added'].fillna("01-Jan-2000")  # placeholder for missing
df['rating'] = df['rating'].fillna("Not Rated")

# -----------------------------
# 3. Remove Duplicates
# -----------------------------
before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]
print(f"\nRemoved {before - after} duplicate rows.")

# -----------------------------
# 4. Standardize Column Names
# -----------------------------
df.columns = df.columns.str.lower().str.replace(" ", "_")

# -----------------------------
# 5. Convert Date Format
# -----------------------------
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# -----------------------------
# 6. Check and Fix Data Types
# -----------------------------
print("\nData Types After Cleaning:\n", df.dtypes)

# -----------------------------
# 7. Save Cleaned Dataset
# -----------------------------
output_path = r"C:\Users\rohit\OneDrive\Desktop\elevate labs\task1\netflix_cleaned.csv"
df.to_csv(output_path, index=False)
print(f"\nCleaned dataset saved as '{output_path}'")

# -----------------------------
# 8. Short Summary Output
# -----------------------------
print("\nCleaning Summary:")
print("- Missing values filled for director, cast, country, date_added, rating")
print("- Duplicate records removed")
print("- Column names standardized")
print("- Date formats converted")
