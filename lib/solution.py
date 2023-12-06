# control_flow.py

def admin_login(username, password):
    if username.lower() == "AD" and password == 12345:
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    if temperature <= 32:
        return "It's brisk out there"
    elif 32 < temperature <= 50:
        return "It's a little chilly out there!"
    elif 50 < temperature <= 80:
        return "It's perfect out there!"
    else:
        return "It's too dang hot out there!"

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def calculator(operation, operand1, operand2):
    if operation == "+":
        return operand1 + operand2
    elif operation == "-":
        return operand1 - operand2
    elif operation == "*":
        return operand1 * operand2
    elif operation == "/":
        if operand2 != 0:
            return operand1 / operand2
        else:
            print("Invalid operation! Division by zero.")
            return None
    else:
        print("Invalid operation!")
        return None
