# elif statement
    # elif statement in Python is stands for "else if".
    # It allows us to check multiple conditions, 
    # providing a way to execute different blocks of code based on which condition is true
age = int(input("Enter the age :"))

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")