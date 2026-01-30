#For loop
    # For loop is iterate over a sequence like list, Tuple, String and range.
    # It allow to execute a block of code repeatedly, once for each item in the sequence.
n = 4
for i in range(0, n):
    print(i)

li = ["Saroj", "Pradyumna", "Prabhu"]
print("This is the list Element")
for x in li:
    print(x)
    
tup = ("Satish", "Pratap", "Prahalad")
print("This is the Tuple Element")
for x in tup:
    print(x)
    
s = "Prabhuprasad"
print("This is the String Element")
for x in s:
    print(x)
    
d = dict({'x':123, 'y':354})
print("This is the Dictonary Element")
for x in d:
    print("%s  %d" % (x, d[x]))
    
set1 = {10, 30, 20}
print("This is the Set Element")
for x in set1:
    print(x)

# Iterating by Index of Sequences
    # We can also use the index of elements in the sequence to iterate.
    #  The key idea is to first calculate the length of the list and
    #  then iterate over the sequence within the range of this length.
li = ["Saroj", "Pradyumna", "Prabhu"]
for index in range(len(li)):
    print(li[index])      