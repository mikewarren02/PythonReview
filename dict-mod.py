# Dictionaries - {Key: Value}

car_make = "chevy"
car_model = "malibu"

car = {"make": "Chevy", "model": "Malibu", "year": "2020"}

# print(car["make"])

# empty dictionary
user = {}

user["first name"] = "John"
user["last name"] = "Doe"

# print(user)


# Activity 1


# create inputs
# first_name = str(input("Enter your first name: "))
# last_name = str(input("Enter your last name: "))
# car_make = str(input("Enter your car make: "))
# car_model = str(input("Enter your car model: "))
# car_year = str(input("Enter your car year: "))


# # create dictionaries from inputs
# name = {"first_name": first_name, "last_name": last_name}
# car = {"make": car_make, "model": car_model, "year": car_year}

# # array containing two dictionaries
# user = {"name": name, "car": car}

# printing statement
# print(f"My name is {name['last_name']}, {name['first_name']}")
# print(f"I have a {car['year']} {car['make']}, {car['model']}")
# print(user)


# Activity 2 nested dictionary (dictionary with dictionaries in it)

family = [
    {
        "Parents": "Mike & Murrie",
        "Siblings": {
            "Brothers": "Mekhi & Malik",
            "Sisters": "Nyeema & Najae"
        },
        "Grandmas": "Angela & Ceola",
        "Pets": "Dior"
    }
]

# print(family)

# iterating through dictionary using loop

# # option 1 
# for key in family:
#     print(family[key])


# # option 2 
# for value in family.values():
#     print(value)


# # option 3
# for key, value in family.items():
#     print(key)
#     print(value)


# delete in dictionary

electric_car = {"make": "Tesla", "model": "Model S"}
print(electric_car)

del electric_car["model"]
print(electric_car)