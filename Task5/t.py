import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------
# 1. Load Dataset
# ---------------------------
df = pd.read_csv(r"C:\Users\rohit\OneDrive\Desktop\elevate labs\Task5\train_and_test2.csv")

# ---------------------------
# 2. Fix column names
# ---------------------------
# Rename wrong '2urvived' column to 'Survived'
df.rename(columns={"2urvived": "Survived"}, inplace=True)

# Optional: Drop unnecessary 'zero' columns
df = df.loc[:, ~df.columns.str.startswith("zero")]

# ---------------------------
# 3. Basic Info & Stats
# ---------------------------
print("--- First 5 Rows ---")
print(df.head())

print("\n--- Info ---")
print(df.info())

print("\n--- Summary Statistics ---")
print(df.describe())

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Value Counts for 'Survived' ---")
print(df['Survived'].value_counts())

# ---------------------------
# 4. Univariate Analysis
# ---------------------------

# Histogram for Age
plt.figure(figsize=(6,4))
sns.histplot(df['Age'], kde=True, bins=30, color='skyblue')
plt.title('Age Distribution')
plt.show()

# Countplot for Survival
plt.figure(figsize=(6,4))
sns.countplot(x='Survived', data=df, palette='pastel')
plt.title('Survival Count')
plt.show()

# Boxplot for Fare
plt.figure(figsize=(6,4))
sns.boxplot(y='Fare', data=df, palette='Set2')
plt.title('Fare Distribution')
plt.show()

# ---------------------------
# 5. Bivariate Analysis
# ---------------------------

# Survival by Gender
if 'Sex' in df.columns:
    plt.figure(figsize=(6,4))
    sns.countplot(x='Survived', hue='Sex', data=df, palette='coolwarm')
    plt.title('Survival by Gender')
    plt.show()

# Survival by Class
if 'Pclass' in df.columns:
    plt.figure(figsize=(6,4))
    sns.countplot(x='Survived', hue='Pclass', data=df, palette='muted')
    plt.title('Survival by Passenger Class')
    plt.show()

# Age vs Fare
plt.figure(figsize=(6,4))
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df, palette='Set1')
plt.title('Age vs Fare (Colored by Survival)')
plt.show()

# ---------------------------
# 6. Multivariate Analysis
# ---------------------------
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

# Pairplot
sns.pairplot(df[['Survived', 'Pclass', 'Age', 'Fare']], hue='Survived')
plt.show()

# ---------------------------
# 7. Observations
# ---------------------------
print("\nOBSERVATIONS:")
print("1. Younger passengers had higher survival rate.")
print("2. Females had a much higher survival rate than males.")
print("3. 1st class passengers survived more than 3rd class passengers.")
print("4. Higher fares are linked with higher survival.")
print("5. Missing values mostly in 'Embarked' column.")
