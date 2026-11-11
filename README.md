Task 5: Exploratory Data Analysis (EDA) --- Titanic Dataset
Project overview
This project explores the Titanic passenger dataset using Python, Pandas, NumPy, Matplotlib and Seaborn. The goal is to understand the dataset, examine missing values and distributions, identify relationships between passenger characteristics and survival, and communicate the findings through visualizations.
This is a descriptive exploratory analysis. Relationships found in the data should not be interpreted as proof of cause and effect.
Project files
Keep these files together in the same folder:
titanic_dataset.csv --- source dataset containing 891 passenger records and 12 columns.
Task_5_Titanic_EDA.ipynb --- Jupyter Notebook containing the analysis code, charts, observations and conclusion.
README.md --- project documentation.
Tools and libraries
Python 3
Jupyter Notebook or JupyterLab
Pandas
NumPy
Matplotlib
Seaborn
Installation
Install the required packages from a terminal or command prompt:
pip install pandas numpy matplotlib seaborn jupyter
How to run the project
Download or place titanic_dataset.csv and Task_5_Titanic_EDA.ipynb in the same folder.
Open a terminal in that folder.
Start Jupyter Notebook:
jupyter notebook
Open Task_5_Titanic_EDA.ipynb.
Select Kernel → Restart & Run All (or Run All) to execute the analysis.
Review the tables, charts, observations and conclusion produced by the notebook.
The notebook reads the CSV using the relative filename titanic_dataset.csv. If the CSV is in a different folder, update the path in the pd.read_csv() statement.
Dataset description
The dataset has 891 rows and 12 original columns:
Column                              Description
PassengerId                       Unique passenger identifier
Survived                          Survival indicator: 0 = did not survive, 1 = survived
Pclass                            Passenger ticket class: 1, 2 or 3
Name                              Passenger name
Sex                               Passenger sex
Age                               Passenger age
SibSp                             Number of siblings or spouses aboard
Parch                             Number of parents or children aboard
Ticket                            Ticket number
Fare                              Passenger fare
Cabin                             Cabin identifier
Embarked                          Port of embarkation
Analysis performed
The notebook carries out the following steps:
Load and inspect data --- reads the CSV, displays the dataset shape and first rows, and checks data types with df.info().
Descriptive statistics --- uses describe(include="all") to summarize the columns.
Missing values and duplicates --- counts missing values and duplicate rows.
Frequency counts --- examines values in Survived, Pclass, Sex, Embarked, SibSp and Parch.
Prepare analysis column --- creates SurvivalStatus labels for chart readability and calculates the overall survival rate.
Univariate analysis --- plots the age distribution and passenger survival counts.
Bivariate analysis --- compares survival rates by sex and passenger class.
Boxplot analysis --- compares fare distributions by survival status.
Scatterplot analysis --- explores age versus fare, coloured by survival status.
Pairplot --- compares selected numeric variables and survival groups.
Correlation heatmap --- visualizes correlations among selected numeric columns.
Findings and conclusion --- summarizes the patterns observed.
Key findings recorded in the notebook
The dataset contains 891 passengers and 12 original columns.
The overall survival rate is approximately 38.4%.
More passengers did not survive than survived.
Female passengers had a substantially higher survival rate than male passengers.
First-class passengers had a higher survival rate than second- and third-class passengers.
Fare values are right-skewed; survivors generally show a higher median fare.
Age and fare do not show a strong simple linear relationship in the scatterplot.
Age has 177 missing values, Cabin has 687 missing values, and Embarked has 2 missing values in the supplied CSV.
The notebook does not silently remove outliers or fill missing values.
These are descriptive observations from this dataset. They do not establish causation.
Expected outputs
When all notebook cells have run successfully, the notebook displays: - Dataset preview, structure and descriptive statistics - Missing-value and duplicate summaries - Frequency-count tables - Age histogram and survival count plot - Survival-rate bar plots by sex and passenger class - Fare boxplot - Age-versus-fare scatterplot - Pairplot - Correlation heatmap - Written observations and conclusion
Notes
Keep the CSV filename exactly as titanic_dataset.csv, unless you also change the filename in the notebook.
The notebook adds a derived SurvivalStatus column during analysis; the original CSV is not modified.
Missing values are reported but are not imputed in this exploratory analysis.
For predictive modelling, decide how to handle missing values and other preprocessing steps before training a model.
Author
Add your name, course, institution and submission date here if required by your assignment.