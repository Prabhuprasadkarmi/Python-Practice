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

# nested if else statement
    # Nested if..else means an if-else statement inside another if statement.
    # We can use nested if statements to check conditions within conditions.
age = int(input("Enter the age :"))
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")