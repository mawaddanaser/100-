# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data["temp"]))
# print(type(data))
#
# data_dic = data.to_dict()
# print(data_dic)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average_temp = sum(temp_list)/ len(temp_list)
# print(average_temp)
#
# print(data["temp"].mean())
# ##############

# # for maximum value of temp
# maximum = data["temp"].max()
# print(maximum)
# #####################

# # Get data in columns
# print(data["condition"]) #using key
# print(data.condition)    #using attribute
#############

# Get data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# temp_F = (monday.temp * 9/5) + 32
# print(temp_F)
############

# Create a DataFrame from scratch
# data_dic = {
#     "students": ["Amy", "Lela", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dic)
# print(data)
# data.to_csv("new_data.csv")
###########
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dic = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dic)
df.to_csv("squirrel_count.csv")