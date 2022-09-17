def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def power(a,b):
    return pow(a,b)

def remainder(a,b):
    return a%b

def select_op(choice):

    if choice == "+":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(add(a,b))
    elif choice == "-":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(subtract(a,b))
    elif choice == "*":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(multiply(a,b))
    elif choice == "/":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(divide(a,b))
    elif choice == "^":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(power(a,b))
    elif choice == "%":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(remainder(a,b))
    elif choice == "#":
        print("Done terminating")
        exit()
    elif choice == "$":
        print("Resetting")
    else:
        print("Incorrect choice")

while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    
    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
    if (select_op(choice) == -1):
        print("Done Terminating")
        exit()

        