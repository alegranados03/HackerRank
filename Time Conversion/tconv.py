#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    s=s.split(':')
    if 'PM' in s[2] and s[0]!='12':
        s[0],s[2]=str(int(s[0])+12),s[2][:2]
    elif 'AM' in s[2] and s[0]=='12':
         s[0],s[2]='00',s[2][:2]
    else:
        s[2]=s[2][:2]
    s=':'.join(s)
    return s


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
