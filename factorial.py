def factorial():
    number = int(input("Pick a Number: "))
    answer = 1
    if number < 0:
        print("There are no factorials for that number, Pick another")
    elif number == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, number + 1):
            # print(f"{answer} = ({answer} * {i}")
            answer = (answer * i)
        print("The factorial of", number, "is", answer)


factorial()
