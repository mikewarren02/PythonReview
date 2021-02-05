def primeOrNot():
    number = int(input("Pick a Number: "))
    if number == 2:
        print(f"{number} is a Prime Number")
        return
    for i in range(2, number):
        if (number % i) == 0:
            print(f"{number} is not Prime Number!")
            break
    
        else:
            print(f"{number} is a Prime Number")
            break


primeOrNot()
