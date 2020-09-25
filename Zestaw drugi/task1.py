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
