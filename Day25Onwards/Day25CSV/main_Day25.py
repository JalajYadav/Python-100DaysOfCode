# with open("./weather_data.csv") as data:
#     data_row=data.readlines()
#     print(data_row)
# import csv


# with open("./weather_data.csv") as data_file:
#     data= csv.reader(data_file)
#
#     temperature = []
#     for row in data:
#         if row[1]!="temp:":
#             temperature.append(row[1])
#     print(temperature)
import pandas

data = pandas.read_csv("./weather_data.csv")
# print(data)
# print(data["temp"])
# print(data.to_dict())
data_list = data["temp"].to_list();
# sum = sum(data_list)
# average = sum/len(data_list)
# print(average)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.temp)
# print(data[data.temp==data.temp.max()])
# TODO:Monday temp in Farenhite
# print("Monday temp in farenhite")
# print((data[data.day=="Monday"].temp*1.8)+32)
data_dict ={
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")