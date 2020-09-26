import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

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
#sns.pairplot(df, kind="scatter")


#Task2
df = pd.read_csv("survey_results_public.csv",
                 usecols=["Respondent","Age", "Hobbyist", "Gender", "WorkWeekHrs", "CodeRevHrs", "ConvertedComp", "YearsCode"],
                 index_col="Respondent")

df.loc[df["YearsCode"] == "Less than 1 year"] = 0
df.loc[df["YearsCode"] == "More than 50 years"] = 51
df["YearsCode"] = df["YearsCode"].astype("float64")

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

df1 = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
print(df1)


#Task4
#linear regression and MSE
reg1 = linear_model.LinearRegression()
reg1.fit(df1[["Age"]], df1["CodeRevHrs"])
print("MSE:", mean_squared_error(df1["CodeRevHrs"], reg1.predict(df1[["Age"]])))

reg2 = linear_model.LinearRegression()
reg2.fit(df1[["Age", "YearsCode"]], df1["CodeRevHrs"])
print("MSE:", mean_squared_error(df1["CodeRevHrs"], reg2.predict(df1[["Age", "YearsCode"]])))

reg3 = linear_model.LinearRegression()
reg3.fit(df1[["Age", "CodeRevHrs", "Gender_Man", "Gender_Woman"]], df1["YearsCode"])
print("MSE:", mean_squared_error(df1["YearsCode"], reg3.predict(df1[["Age", "CodeRevHrs", "Gender_Man", "Gender_Woman"]])))




