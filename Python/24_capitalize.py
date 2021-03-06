#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = list(s.split(' '))
    p=[]
    for i in s:
        if i.isalpha():
            p.append(i[0].upper()+i[1:]+" ")
        else:
            p.append(i)
            p.append(" ")            
    p="".join(p)
    return p

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
