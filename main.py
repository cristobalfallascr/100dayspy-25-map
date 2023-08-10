# with open ("weather_data.csv") as file:
#
#     data = file.readlines()
#     clean_data =[]
#     for data_line in data:
#         print(data_line.strip())
#         clean_data.append(data_line.strip())
#     print(clean_data)
# import csv

#
# with open("weather_data.csv" ) as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)
#
import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
