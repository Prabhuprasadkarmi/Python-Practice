# function in function 
  # function inside function is called nested function
def outer_function():
    print("This is the outer function.")
    
    def inner_function():
        print("This is the inner function.")
    
    inner_function()  # Calling the inner function
outer_function()  # Calling the outer function
