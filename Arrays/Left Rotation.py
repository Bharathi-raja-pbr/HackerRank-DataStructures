'''
A left rotation operation on an array of size N shifts each of the array's elements 1 unit to the left. Given an integer,D ,
rotate the array that many steps left and return the result.

Example

arr=[1,2,3]

After 1 rotations,[2,3,1] .

Function Description

Complete the rotateLeft function in the editor below.

rotateLeft has the following parameters:

int d: the amount to rotate by
int arr[n]: the array to rotate

Returns
int[n]: the rotated array

Input Format

The first line contains two space-separated integers that denote , N the number of integers, and d, the number of left rotations to perform.
The second line contains N space-separated integers that describe arr.

Constraints
1<=n<=10^5
Sample Input

5 4
1 2 3 4 5
Sample Output

5 1 2 3 4

'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    # Write your code here
    val=[]
    n=len(arr)
    d=d%n
    
    for i in range(0,n):
        val.append(arr[(i+d)%n])
    return val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
