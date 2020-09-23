import pandas as pd

#Task1
df = pd.read_csv("train.tsv", sep = '\t')
colNames = ["Price", "Number_of_rooms", "Square_footage", "Floor_number", "Address", "Description"]
df.columns = colNames

#Calculate mean price and save file
mean = int(df['Price'].mean()*1000)

with open("./out0.csv", 'w') as out0:
    out0.write(str(mean))

#Task2
#Calculate price per square meter
df['Price_per_square_meter'] = df['Price']/df['Square_footage']

#rows
rooms = df["Number_of_rooms"] >= 3
price = df["Price_per_square_meter"] < df["Price_per_square_meter"].mean()

#columns
df1 = pd.DataFrame(df[rooms & price], columns=["Number_of_rooms", "Price", "Price_per_square_meter"])

df1.to_csv("out1.csv", header=0)