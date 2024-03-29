import pandas as pd
# data = pd.read_csv("/Users/pranaymathur/Desktop/100daysPython/day25/weather_data.csv")
# monday = (data[data.day == "Monday"])
# print(monday.temp)
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

dict = {
    "furcolor":["Gray", "Cinnamon", "Black"],
    "count":[gray, red, black]
}

new = pd.DataFrame(dict)
new.to_csv("furcolor.csv")
