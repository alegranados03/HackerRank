#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    b=sum(arr)
    minim,maxim =b-arr[len(arr)-1],b-arr[0]
    print(str(minim)+' '+str(maxim))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
