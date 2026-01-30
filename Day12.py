# Ternary condition statement
    # this is the compact way of if-else statement in single line 
# Assign a value based on a condition
age = int(input("Enter the age:"))
s = "Adult" if age >= 18 else "Minor"
print(s)

# Match-Case Statement
    # match-case statement is Python's version of a switch-case found in other languages.
    # It allows us to match a variable's value against a set of patterns.
number =int(input("Enter the number:"))

match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("three")    
    case _:
        print("Other number")

 # Loops in Pyhton (for,while,nested loops)
    # Loops in the Python used for repeat action efficiently.
    # The main types are For loops (counting through items) and While loops (based on conditions).
#For loop
    # For loop is iterate over a sequence like list, Tuple, String and range.
