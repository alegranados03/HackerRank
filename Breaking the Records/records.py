#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    cmin,cmax,minim,maxim=0,0,scores[0],scores[0]

    for x in scores:
        if(x<minim):
            cmin+=1
            minim=x
        elif(x>maxim):
            cmax+=1
            maxim=x
        else:
            pass
    return[cmax,cmin]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
