
def calculator():
    first_no = float(input("First number: "))
    operation = input("Operation: ")
    second_no = float(input("Second number: "))

    if operation == "+":
        total = first_no + second_no
        print(total)
    elif operation == "-":
        total = first_no - second_no
        print(total)

    elif operation == "/":
        total = first_no / second_no
        print(total)

    elif operation == "*":
        total = first_no * second_no
        print(total)


calculator()
