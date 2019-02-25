#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    print('{}\n{}\n{}\n'.format(
        len([arr[i] for i in range(len(arr)) if arr[i]>0])/len(arr),
        len([arr[i] for i in range(len(arr)) if arr[i]<0])/len(arr),
        len([arr[i] for i in range(len(arr)) if arr[i]==0])/len(arr),
    )
    )

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
