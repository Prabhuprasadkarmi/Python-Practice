# function in function 
  # function inside function is called nested function
def outer_function():
    print("This is the outer function.")
    
    def inner_function():
        print("This is the inner function.")
    
    inner_function()  # Calling the inner function
outer_function()  # Calling the outer function

# recursive function
    # A recursive function is a function that calls itself in order to solve a problem.
    # It typically has a base case that stops the recursion and a recursive case that breaks the problem into smaller subproblems.   
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) 
print("The factorial of 5 is:", factorial(5))