# Sequence datatypes

# A sequence is an ordered collection of items, which can be of similar or different data types. 
# Sequences allow storing of multiple values in an organized and efficient fashion.
# There are several sequence data types of Python:

# String datatype

# Python Strings are arrays of bytes representing Unicode characters.
#  In Python, there is no character data type, a character is a string of length one. It is represented by str class.

# Strings in Python can be created using single quotes, double quotes or even triple quotes.
# We can access individual characters of a String using index.

s = 'Welcome to the Real World'
print(s)

# check data type 
print(type(s))

# access string with index
print(s[1])
print(s[2])
print(s[-1])

# List Data Type

# Lists are similar to arrays found in other languages. 
# They are an ordered and mutable collection of items. 
# It is very flexible as items in a list do not need to be of the same type.

# Creating a List in Python

# Lists in Python can be created by just placing sequence inside the square brackets[].




# Empty list
a = []
print(a)
# list with int values
a = [1, 2, 3]
print(a)
# list with mixed values int and String
b = ["Raja", "Babu", "karmi", 4, 5]
print(b)