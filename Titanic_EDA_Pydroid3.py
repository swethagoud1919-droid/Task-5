# TASK 5: EXPLORATORY DATA ANALYSIS (EDA) - TITANIC DATASET
# Run this file in Pydroid 3.
# First install required libraries in Pydroid 3:
# pip install pandas matplotlib seaborn

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 60)
print("TASK 5 - EXPLORATORY DATA ANALYSIS (TITANIC)")
print("=" * 60)

# 1. LOAD DATASET
# The program downloads the Titanic CSV automatically the first time.
DATA_URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
DATA_FILE = "titanic.csv"

try:
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        print("\nDataset loaded from local file:", DATA_FILE)
    else:
        print("\nDownloading Titanic dataset...")
        df = pd.read_csv(DATA_URL)
        df.to_csv(DATA_FILE, index=False)
        print("Dataset downloaded and saved as:", DATA_FILE)
except Exception as error:
    print("\nCould not download the dataset.")
    print("Check your internet connection and run the program again.")
    print("Error:", error)
    raise SystemExit

# 2. BASIC DATA EXPLORATION
print("\n1. FIRST FIVE ROWS")
print(df.head())

print("\n2. LAST FIVE ROWS")
print(df.tail())

print("\n3. DATASET SHAPE (ROWS, COLUMNS)")
print(df.shape)

print("\n4. COLUMN INFORMATION")
df.info()

print("\n5. STATISTICAL SUMMARY")
print(df.describe(include="all"))

print("\n6. MISSING VALUES")
print(df.isnull().sum())

print("\n7. DUPLICATE ROWS")
print(df.duplicated().sum())

print("\n8. SURVIVAL COUNTS")
print(df["Survived"].value_counts())

print("\n9. PASSENGER CLASS COUNTS")
print(df["Pclass"].value_counts())

print("\n10. GENDER COUNTS")
print(df["Sex"].value_counts())

# 3. DATA CLEANING
print("\n" + "=" * 60)
print("DATA CLEANING")
print("=" * 60)

# Fill missing numerical values with median.
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Fare"] = df["Fare"].fillna(df["Fare"].median())

# Fill missing categorical values with mode.
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Cabin has many missing values; mark missing entries as Unknown.
df["Cabin"] = df["Cabin"].fillna("Unknown")

# Remove duplicate rows, if any.
df = df.drop_duplicates()

print("\nMissing values after cleaning:")
print(df.isnull().sum())
print("\nDataset shape after cleaning:", df.shape)

# Save cleaned data.
df.to_csv("titanic_cleaned.csv", index=False)
print("Cleaned dataset saved as titanic_cleaned.csv")

# 4. UNIVARIATE ANALYSIS
sns.set_theme(style="whitegrid")

plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Survived")
plt.title("Survival Count (0 = No, 1 = Yes)")
plt.xlabel("Survived")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("01_survival_count.png")
plt.show()

plt.figure(figsize=(7, 5))
sns.histplot(df["Age"], bins=25, kde=True)
plt.title("Distribution of Passenger Age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("02_age_histogram.png")
plt.show()

plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Pclass")
plt.title("Passenger Count by Ticket Class")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("03_passenger_class.png")
plt.show()

# 5. BIVARIATE ANALYSIS
plt.figure(figsize=(7, 5))
sns.barplot(data=df, x="Sex", y="Survived")
plt.title("Average Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate")
plt.tight_layout()
plt.savefig("04_survival_by_gender.png")
plt.show()

plt.figure(figsize=(7, 5))
sns.barplot(data=df, x="Pclass", y="Survived")
plt.title("Average Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.tight_layout()
plt.savefig("05_survival_by_class.png")
plt.show()

plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x="Pclass", y="Fare")
plt.title("Ticket Fare by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Fare")
plt.tight_layout()
plt.savefig("06_fare_boxplot.png")
plt.show()

plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x="Age", y="Fare", hue="Survived", alpha=0.7)
plt.title("Age vs Fare (Colored by Survival)")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.tight_layout()
plt.savefig("07_age_fare_scatterplot.png")
plt.show()

# 6. CORRELATION HEATMAP
numeric_df = df.select_dtypes(include="number")
plt.figure(figsize=(9, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("08_correlation_heatmap.png")
plt.show()

# 7. PAIRPLOT
# Use a sample to keep plotting faster on a mobile phone.
pair_columns = ["Survived", "Pclass", "Age", "Fare"]
pair_data = df[pair_columns].sample(
    n=min(250, len(df)), random_state=42
)
pair_plot = sns.pairplot(pair_data, hue="Survived", diag_kind="hist")
pair_plot.fig.suptitle("Pairplot of Titanic Dataset", y=1.02)
pair_plot.savefig("09_pairplot.png")
plt.show()

# 8. GROUP ANALYSIS
print("\n" + "=" * 60)
print("GROUP ANALYSIS")
print("=" * 60)

print("\nSurvival rate by gender:")
print(df.groupby("Sex", observed=False)["Survived"].mean().round(3))

print("\nSurvival rate by passenger class:")
print(df.groupby("Pclass", observed=False)["Survived"].mean().round(3))

print("\nAverage age by passenger class:")
print(df.groupby("Pclass", observed=False)["Age"].mean().round(2))

# 9. AUTOMATIC SUMMARY
total = len(df)
survivors = int(df["Survived"].sum())
not_survived = total - survivors
survival_rate = (survivors / total) * 100

gender_rates = df.groupby("Sex", observed=False)["Survived"].mean() * 100
class_rates = df.groupby("Pclass", observed=False)["Survived"].mean() * 100

print("\n" + "=" * 60)
print("FINAL SUMMARY OF FINDINGS")
print("=" * 60)
print("Total passengers:", total)
print("Passengers who survived:", survivors)
print("Passengers who did not survive:", not_survived)
print("Overall survival rate: {:.2f}%".format(survival_rate))
print("Survival rate by gender (%):")
print(gender_rates.round(2))
print("Survival rate by passenger class (%):")
print(class_rates.round(2))

print("\nOBSERVATIONS")
print("1. The dataset contains passenger and travel information.")
print("2. The Age, Cabin and Embarked columns contain missing values in the original data.")
print("3. Missing Age and Fare values were filled using the median.")
print("4. Missing Embarked values were filled using the most frequent value.")
print("5. The gender and passenger-class charts help compare survival rates.")
print("6. The heatmap shows correlations between numerical columns.")
print("7. The plots help identify distributions, relationships and unusual values.")

print("\nEDA TASK COMPLETED SUCCESSFULLY!")
print("Files created: titanic.csv, titanic_cleaned.csv and chart PNG files.")
