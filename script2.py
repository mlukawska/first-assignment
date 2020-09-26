import pandas as pd

df = pd.read_csv("train.tsv", sep = '\t',
                 names = ["Price", "Number_of_rooms", "Square_footage", "Floor_number", "Address", "Description"])

df_description = pd.read_csv("description.csv")

#merging data frames
new_df = df.merge(df_description, left_on='Floor_number', right_on='liczba', how='left')

#new data frame with selected columns without conflict
new_df2 = pd.DataFrame(df, columns=["Price", "Number_of_rooms", "Square_footage", "Floor_number", " opis", "Address", "Description"])

new_df2.to_csv("out2.csv")