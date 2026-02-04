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
    # Default arguments allow a function to have default values for parameters if no argument is provided during the function call.
def greet_user(name="Guest"):
    print("Hello, " + name + "! Welcome to Python programming.")
greet_user()  # Uses default argument
greet_user("Prabhuprasad Karmi")  # Uses provided argument
# Function with Variable-length Arguments
    # The *args parameter allows a function to accept any number of positional arguments.
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total 
total_sum = sum_numbers(1, 2, 3, 4, 5)
print("The total sum is:", total_sum)
# Lambda Function
    # A lambda function is a small anonymous function that can take any number of arguments but can only have one expression.
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
    # The map() function applies a given function to all items in an iterable (like a list) and returns a map object (an iterator).
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print("Squared numbers:", squared_numbers)
# Function Annotations
    # Function annotations provide a way of associating various parts of a function with arbitrary Python expressions at compile time.
def add_numbers(a: int, b: int) -> int:
    return a + b  
print("The sum using annotated function is:", add_numbers(10, 20))