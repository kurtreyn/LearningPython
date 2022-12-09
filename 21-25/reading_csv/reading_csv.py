import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)

# ** FOR MORE COMPLEX DATA USE PANDA
import pandas

# ** DataFrames in pandas is like the entire data table
# ** Series in pandas is like the columns in the table

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(temp_list)

avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)

avg_temp_using_mean = data["temp"].mean()
# print(avg_temp_using_mean)

max_temp = data["temp"].max()
# print(max_temp)

# To get data in a column: data["name_of_col"] or data.name_of_col
# print(data["temp"])
# print(data.temp)


# To get data in a row:
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
# print(monday.condition)
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create a dataframe from scratch:
data_dict_two = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

new_data = pandas.DataFrame(data_dict_two)
# print(new_data)
new_data.to_csv("new_data.csv")