# Python Set Datatype
    # set is unorder collection of data , where the data has not duplicate value.

# initializing empty set
s1 = set()

s1 = set("Prabhuprasad Karmi")              # here space is count as a object
print("Set with the use of String: ", s1) 

s2 = set(["Saroj", "Prabhu", "Pradyumna"])
print("Set with the use of List: ", s2)

# Access the set datatypes
""" Set items cannot be accessed by referring to an index, 
     since sets are unordered the items have no index. But we can loop through the set items using a for loop, 
     or ask if a specified value is present in a set, by using the keyword in."""

set1 = set(["Saroj", "Prabhu", "Pradyumna","Prabhu"]) #Duplicates are removed automatically
print(set1) 

# loop through set
for i in set1:
   print(i, end=" ") #prints elements one by one
  
# check if item exist in set   
print( "Prabhu" in set1)

# Python Dictonary
    # Python dictonary is the collection of data values
    #  a Dictionary holds a key: value pair.
    # dictonary is store the value using the column(:) and separated by comma(,)

# create the Dictonary 
    # values in the dictonary can be any datatype and duplicate.
    # key can't be duplicate.

# initialize empty dictionary
d = {}

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1) 