# nested loop
    # Python programming language allows to use one loop inside another loop which is called nested loop.
from __future__ import print_function
for i in range(1, 6):
    for j in range(i):
        print(i, end=' ')
    print()
# Compound assignment operators
x = 10 
x += 2  # equivalent to x = x + 2 here we are adding 2 to the value of x . x is now 12
x -= 5  # equivalent to x = x - 5 here we are subtracting 5 from the value of x . x is now 7
x *= 3  # equivalent to x = x * 3 here we are multiplying 3 to the value of x . x is now 21
# x /= 4  # equivalent to x = x / 4 here we are dividing 4 to the value of x . x is now 5.25
# x -= 4  # equivalent to x = x - 4 here we are subtracting 4 from the value of x . x is now 1.25
print(x)
