import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Task1
df = pd.read_csv("survey_results_public.csv",
                 usecols=["Respondent","Age", "WorkWeekHrs", "CodeRevHrs", "ConvertedComp", "YearsCode"],
                 index_col="Respondent")

#delete null records
df.dropna(inplace=True)

#convert to numeric data and change type to float64
df.loc[df["YearsCode"] == "Less than 1 year"] = 0
df.loc[df["YearsCode"] == "More than 50 years"] = 51
df["YearsCode"] = df["YearsCode"].astype("float64")

#check types
type_obj = df.dtypes
print(type_obj)

#dependency table
print(df.corr())

#plots
sns.pairplot(df, kind="scatter")


#Task2
df = pd.read_csv("survey_results_public.csv",
                 usecols=["Respondent","Age", "Hobbyist", "Gender", "WorkWeekHrs", "CodeRevHrs", "ConvertedComp", "YearsCode"],
                 index_col="Respondent")

df.dropna(inplace=True)
df["Gender"] = df["Gender"].astype("str")

#convert to numeric data
map_function = {"Yes": 1, "No": 0}
df['Hobbyist'] = df['Hobbyist'].map(map_function)

#one-hot encoding
df = df[(df["Gender"] == "Man") | (df["Gender"] == "Woman")]
df = pd.get_dummies(df, columns=["Gender"])
print(df)


#Task3
#removing outliers
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

df = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
print(df)
