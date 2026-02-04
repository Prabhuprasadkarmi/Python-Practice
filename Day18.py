# Python Function 
  # A function is a block of reusable code that performs a specific task.
  # Functions help in breaking down complex problems into smaller, manageable parts.    
# Defining a Function
def greet(name):
    print("Hello, " + name + "! Welcome to Python programming.") 
# Calling a Function
greet("Prabhuprasad Karmi")
# Function with Return Value
def add(a, b):
    return a + b
result = add(5, 10)
print("The sum is:", result)
# Function with Default Arguments
def greet_user(name="Guest"):
    print("Hello, " + name + "! Welcome to Python programming.")
greet_user()  # Uses default argument
greet_user("Prabhuprasad Karmi")  # Uses provided argument
# Function with Variable-length Arguments
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total 
total_sum = sum_numbers(1, 2, 3, 4, 5)
print("The total sum is:", total_sum)
# Lambda Function
square = lambda x: x * x
print("The square of 5 is:", square(5))
# Recursive Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("The factorial of 5 is:", factorial(5))
# Anonymous Function with map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print("Squared numbers:", squared_numbers)