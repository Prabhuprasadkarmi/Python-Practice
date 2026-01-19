#1 This is the first Program of the Python 
print("hello world!")

#2 Python input and output 

name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")

# output 

# Enter your name: Prabhu
# Hello, Prabhu ! Welcome! 

#3 Python printing variable

# variable is the container of the data which can be manipulated at the time of program execution

#3.1 integer 
a = 10
print(a)

#3.2 string 
name = "Prabhu"
print(name)

#3.3 double
b = 2.4
print(b)


#4 multiple variable output 
print(a,name,b)


#5 Take multiple input 

# *** splitting the values entered by
#  the user into separate variables for each value using the split() method

x, y = input("Enter number of boys and girls: ").split()   #  where split() used the space as separation
print("Number of boys: ", x)
print("Number of girls: ", y)
 
x, y, z = input("Enter total no. of student and boys and girls: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)

#Find DataType of Input in Python
print(a)
print(type(a))

#6 change the type of input 

# *** by deafault python input() read the user input as string 

n = int(input("Enter a number: "))  #this called as the typecasting 
print(n)
print(type(n))

