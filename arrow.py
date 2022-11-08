import numpy as np
import os
import time

s= ""

matrix=[[' ']*17]

for i in range(5):
    s+=" "*11
    s+="*"*(i+1)
    s+=' '*((5-i)+17)
    s=list(s)
    matrix.append(s)
    s=''

s+="*"*17
s+=' '*(17)
s=list(s)
matrix.append(s)
s=''
for i in range(5):
    s+=" "*11    
    s+="*"*(5-i)
    s+=' '*((i+1)+17)
    s=list(s)
    matrix.append(s)
    s=''

for i in range(10):
    for s in matrix:
        for c in s:
            print(c, end='')
        print()

    matrix = list(zip(*reversed(matrix)))
    time.sleep(1.5)
    os.system('cls')