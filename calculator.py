# Functions for Add, Sub, Multiply, Divide
def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def dividation(x,y):
    return x/y

#Calculation Functionality
#Showing information to user regarding calculator
def calculation():
    print("Welcome to the Calculator - Please select your desire Option:")
    print("Select 1 for Addition of two numbers:")
    print("Select 2 for Subtraction of two numbers:")
    print("Select 3 for Multiplication of two numbers:")
    print("Select 4 for Dividation of two numbers:")
    
    # Getting input from user for Option
    userChoise = input("Enter your desire option 1/2/3/4: ")
    
    if userChoise == '1' or userChoise == '2' or userChoise == '3' or userChoise == '4':
        num1 = int(input("Please Enter First Number: "))
        num2 = int(input("Please Enter Second Number: "))
        
        if userChoise == '1':
            print(num1, "+", num2, "=", int(addition(num1,num2)), "\n"+"Thank you")
        elif userChoise == '2':
            print(num1, "-", num2, "=", int(subtraction(num1,num2)), "\n"+"Thank you")
        elif userChoise == '3':
            print(num1, "x", num2, "=", int(multiplication(num1,num2)), "\n"+"Thank you")
        elif userChoise == '4':
            print(num1, "/", num2, "=", int(dividation(num1,num2)), "\n"+"Thank you")
        else:
            print("Please Enter the Valid Numaric Digit!")
    else:
        print("Please Enter the number according to the selection 1 or 2 or 3 or 4")
    again() #Again Function to start again

calculation()

#Again Functionality
def again():
    calcAgain = input("Do you want to Calculate Again? Press type 'Y' for YES & 'N' for NO: ")
    
    if calcAgain == "Y":
        calculation()
    elif calcAgain == "N":
        print("Thanks for using the Calculator, See you later.")
    else:
        again()

