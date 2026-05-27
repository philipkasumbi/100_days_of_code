import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260527.csv")
# get row in data
Gray_count = len(data[data["Primary Fur Color"]== 'Gray'])
Black_count = len(data[data["Primary Fur Color"]== 'Black'])
Cinnamon_count = len(data[data["Primary Fur Color"]== 'Cinnamon'])


data_dict = {
    "Fur Color":["Black","Gray","Cinnamon"],
    "Count":[Black_count,Gray_count,Cinnamon_count]
}

data = pandas.DataFrame(data_dict)

data.to_csv("new_data.csv")