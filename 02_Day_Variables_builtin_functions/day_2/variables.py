#'Day 2: 30 Days of python programming'

#level 1
first_name = "Gru"
last_name = "Villano"
full_name = first_name + " " + last_name
country = "Evilland"
city = "cianotopia"
age = "67"
year = "1964"
is_married =  False
is_true = True
is_light = False
nickname, colour, animal = "Book", "brown", "dog"

#level 2
print(type(first_name))
print(type(first_name), type(last_name), type(full_name), type(country),type(city),type(age),type(year), type(is_married), type(is_true), type(is_light), type(nickname))
print(len(first_name))
print(len(first_name) == len(last_name))

num_one = 5
num_two = 4
print(num_one - num_two)
print(num_one + num_two)
print(num_one * num_two)
print(num_two / num_two)
print(num_one % num_two)
print(num_one * num_two)
print(num_one // num_two)

import math
area_of_circle = 3.14159 * 30**2
area_of_circle_math = math.pi * 30**2
print(area_of_circle)
print(area_of_circle_math)

circum_of_circle = 2*math.pi*30
print(circum_of_circle)

radius = 30
user_area = radius
user_circle = user_area**2 * math.pi
print(user_circle)

#input([])
#user_circle = user_area**2 * math.pi
#print(user_circle)

#name, last name, country and age
in_name = input(["name"])
in_last_name = input(["last name"])
in_country = input(["country"])
in_age = input(["age"])
print(f"your name is "+ in_name)
print(f"your last name is " +in_last_name)
print(f"your country is " +in_country)
print(f"your age is " +in_age)


print(help('keywords'))