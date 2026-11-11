Task 5 – Exploratory Data Analysis (EDA): Titanic Dataset
Objective
Explore the Titanic passenger dataset using statistical summaries and visualizations to identify patterns, trends, missing values, and possible outliers.
Project contents
notebooks/Task5_Titanic_EDA.ipynb – step-by-step Jupyter Notebook
eda_titanic.py – complete Python script
data/ – dataset is downloaded here automatically on first run
outputs/ – charts, cleaned dataset, and summary CSV are saved here after running
EDA_Report.pdf – short project report
requirements.txt – required Python libraries
Dataset
This project uses the public Titanic training dataset (891 rows, 12 columns). Source: https://github.com/datasciencedojo/datasets Raw CSV: https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
The notebook/script downloads the CSV automatically if data/titanic.csv is not present. Internet access is required for the first run. You can also download the CSV manually and place it inside the data folder with the name titanic.csv.
How to run
Option 1: Jupyter Notebook
Download or clone this repository.
Install dependencies: pip install -r requirements.txt
Open notebooks/Task5_Titanic_EDA.ipynb in Jupyter Notebook or Google Colab.
Run all cells from top to bottom.
Option 2: Python script
Open a terminal in the project folder.
Run pip install -r requirements.txt
Run python eda_titanic.py
Android / Pydroid 3
Install the packages listed in requirements.txt using Pydroid's Pip screen. Keep the project folders together, open eda_titanic.py, and run it. The first run needs internet to download the CSV.
Analysis performed
Dataset shape, data types, info(), and describe()
Missing-value and duplicate checks
Data cleaning using median and mode imputation
Count plot and age histogram
Survival comparisons by sex and passenger class
Fare boxplot and age-fare scatterplot
Correlation heatmap and pairplot
Export of cleaned dataset and EDA summary
Main observations
The commonly used Titanic training dataset contains 891 passenger records.
The overall survival rate is approximately 38.4%.
Female passengers had a higher survival rate than male passengers.
First-class passengers generally had a higher survival rate than third-class passengers.
Age and Cabin have missing values; Cabin has many missing entries.
Fare values are right-skewed and include high-value observations.
Note: Findings describe associations in this historical sample. They do not establish cause and effect.
GitHub upload
Extract the ZIP file.
Open GitHub and create a new repository, for example Task-5-Titanic-EDA.
Upload the files and folders from this project (not the ZIP file itself).
Add a repository description: Exploratory Data Analysis of Titanic passenger data using Python, Pandas, Matplotlib and Seaborn.
Commit the files.
Interview questions
What is EDA? EDA is the process of examining data using statistics and visualizations before further analysis.
Which plots help check correlation? A correlation heatmap and pairplot are useful for numeric relationships.
How do you handle skewed data? Inspect the distribution, consider a log transformation when appropriate, and use robust statistics such as the median.
How can multicollinearity be detected? Check correlation between predictors and use VIF for a more formal check.
What are univariate, bivariate, and multivariate analyses? They examine one, two, and three or more variables respectively.
Heatmap vs pairplot? A heatmap summarizes pairwise numeric correlation; a pairplot shows pairwise scatterplots and distributions.
How do you summarize insights? Report key patterns, missing values, outliers, limitations, and conclusions supported by charts/statistics.# Task-5