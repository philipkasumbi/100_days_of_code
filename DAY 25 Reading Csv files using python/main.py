# import csv
# with open("C:/Users/kasum/OneDrive/Desktop/100 days of code/DAY 25 Reading Csv files using python/weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

# average temperature
temp_list = data["temp"].tolist()
temp_sum = sum(temp_list)
temp_len = len(temp_list)
average = temp_sum/temp_len
print(average)

print(data['temp'].mean())
print(data['temp'].max())

# get data in columns
print(data.condition)
print(data['condition'])

# get data in row
print(data[data.day == "Monday"])
max_temp = data['temp'].max()
print(data[data.temp == max_temp])

# monday temp into Fahrenheit
monday = data[data.day == "Monday"]
mon_temp = (monday.temp * 1.8)+32
print(mon_temp)

# create a dataframe form scratch
data_dict = {
    "students":["phil","tabi","mercy"],
    "scores":[76,70,30]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")