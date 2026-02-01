# nested loop
    # Python programming language allows to use one loop inside another loop which is called nested loop.
from __future__ import print_function
for i in range(1, 6):
    for j in range(i):
        print(i, end=' ')
    print()