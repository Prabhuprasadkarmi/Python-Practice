#1. swapping the two number without using the third variable

a,b = 5, 10
a,b = b,a
print(a,b)

#2. print the length of the string using len()

name = "Prabhuprasad Karmi"                   # here the space is count as the length
length = len(name)
print("the length of the name :",length)

#3. Calculator using python

a = int(input("Enter the first no.:"))
b = int(input("Enter the second no.:"))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b) 

#4. Calculate the area of circle

from pconst import const 
const.pi = 3.14
radius = float(input("Enter the radius :"))
area = const.pi*radius*radius
print("Area of the circle is",area)