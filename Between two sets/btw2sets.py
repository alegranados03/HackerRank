#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    ct=0
    f=set()
    setfin=set()
    rs=[x for x in range(a[len(a)-1],b[0]+1)]
    for x in rs:
        for elem in a:
            if x%elem==0:
                ct+=1
        if ct==len(a):
            f.add(x)
        ct=0
    for x in f:
        for elem in b:
            if elem%x==0:
                ct+=1
        if ct==len(b):
            setfin.add(x)
        ct=0
    return len(setfin)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
