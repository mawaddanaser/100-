#Python Dictionary
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

#Retrieving item from dictionary
print(programming_dictionary["Function"])

#adding new item to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

#create an empty dictionary
empty_dictionary = {}
print(empty_dictionary)

#wipe an existing dictionary
#programming_dictionary = {}
#print(programming_dictionary)

#Edit an item in the dictionary
programming_dictionary["Bug"] = "a moth in your computer"
print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

  #####################################

#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting a Dictionary in a Dictionary
travei_log = {
  "France" : {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visites" : 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists
# two dict. inside one list, each dictionary has three keys with three different value

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]