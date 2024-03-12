  #Project --- Calculator


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


print("Options:")
print("Enter '+' for addition")
print("Enter '-' for subtraction")
print("Enter '*' for multiplication")
print("Enter '/' for division")
print("Enter 'quit' to end the program")
while(1):
    
   user_input = input("::::: > ")

   if user_input == "quit":
       break
   elif user_input in ["+", "-", "*", "/"]:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if user_input == "+":
            print("Result:", add(x, y))
        elif user_input == "-":
            print("Result:", subtract(x, y))
        elif user_input == "*":
            print("Result:", multiply(x, y))
        elif user_input == "/":
            print("Result:", divide(x, y))
else:
        print("Invalid input. Please enter a valid operation.")
