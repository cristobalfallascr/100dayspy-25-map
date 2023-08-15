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

#data = pandas.read_csv("weather_data.csv")
# #You can specify the name of column to read data
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# total_temp = 0
# for temp in temp_list:
#     total_temp += temp
# avg_temp = total_temp / len(temp_list)
# print("average temperature: "+str(avg_temp))
# avg_temp = sum(temp_list)/len(temp_list)
# print("average temperature: "+str(avg_temp))
#
# avg_temp = data["temp"].mean()
# print("average temperature: "+str(avg_temp))
# max_temp = data['temp'].max()
# print("Max temperature: "+str(max_temp))
#
# #Get data in Colums
# print(data['condition'])
# print(data.condition)
#
# #get data in rows
# print(data[data.day=='Monday'])
# print("Day with highest temperature: ")
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# celsius = monday.temp
#
# farenheit = int(celsius)* 9/5 + 32
# print(farenheit)

#Create df from scratch

# data_dic = {
#     "fruits": ["bananas", "apples","oranges"],
#     "price": [500,1990,2500]
# }
#
# data = pandas.DataFrame(data_dic)
# print(data)
# data.to_csv("fruits-list.csv")
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_fur_colors = data['Primary Fur Color'].tolist()

##Another way is to filter each color individually
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
##

cinnamon = squirrel_fur_colors.count('Cinnamon')
gray = squirrel_fur_colors.count('Gray')
black = squirrel_fur_colors.count('Black')

squirrel_data = {
    "Fur Color": ["Cinnamon", "Gray", "Black"],
    "Squirrel Count": [cinnamon,gray,black]
}

squirrel_df = pandas.DataFrame(squirrel_data)
print(squirrel_df)
squirrel_df.to_csv("Squirrel-summary.csv")


