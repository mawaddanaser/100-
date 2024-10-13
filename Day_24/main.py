# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()

###########
# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)
#mood is r by default
############
with open("my_file.txt", mode="a") as file:
    file.write("\n new text")
############
#To create a new file
# with open("my_file.txt", mode="w") as file:
#     file.write("new textt")
