#Program for receiving input and Implementing a division operation
try :

    numb1 = int(input("Enter the first number: "))
    numb2 = int(input("Enter the second number: "))

    result = numb1 / numb2
    print("Result: ", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
