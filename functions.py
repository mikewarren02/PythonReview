# first_name = "Mike"
# last_name = "Warren"


# def display_user():
#     print("**********")
#     print(f"My first name is {first_name} and last name is {last_name}")
#     print("**********")


# #display_user()

# def greet(name, age):
#     print(f"Hello {name} you are {age} years old")

# greet("Mike", 18)
# greet("Murrie", 37)
# greet("Najae", 24)


# def calculate_overdraft_fee(amount):
#     return amount * 0.10
#     print("Not executed")

# overdraft_fee = calculate_overdraft_fee(100)
# if overdraft_fee > 20:
#     print("lock the account")

# def add(no1, no2):
#     return no1 + no2

# result = add(2,3)
# print(result)


amount = float(input("What is your total: "))
tip_percentage = float(input("What is your prefered tip percentage: "))


def calculate_tip(total, tip):
    return total * (tip/100)


tip_amount = calculate_tip(amount, tip_percentage)

total_bill = tip_amount + amount

statement = f"Thank you for tipping ${tip_amount}, Your new total will be ${total_bill }"

print(statement)
