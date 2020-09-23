import pandas as pd
import matplotlib.pyplot as plot

df_schema = pd.read_csv("survey_results_schema.csv")
df_public = pd.read_csv("survey_results_public.csv",
                        usecols=["Respondent", "Age", "WorkWeekHrs", "CodeRevHrs"],
                        index_col="Respondent")

type_obj = df_public.dtypes
print(type_obj)

#delete null records
df_public.dropna(inplace=True)

#plot
plot.scatter(df_public["Age"], df_public["CodeRevHrs"])
plot.title("Code Review Hours depending on Age")
plot.xlabel("Age")
plot.ylabel("Code Review Hours")
plot.show()

