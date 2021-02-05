
def fizz_buzz():

    number = int(input("What number did you select: "))

    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz ")
    else:
        print("Not an option")

fizz_buzz()
