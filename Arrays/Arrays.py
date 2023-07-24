'''

An array is a type of data structure that stores elements of the same type in a contiguous block of memory.
In an array, arr, of size ,N each memory location has some unique index, i (where 0<=i<len(arr), that can be referenced as arr[i]  or ai.

Reverse an array of integers.

Example
A=[1,2,3]
Return [3,2,1] .

Function Description

Complete the function reverseArray in the editor below.

reverseArray has the following parameter(s):
int A[n]: the array to reverse

Returns 
int[n]: the reversed array

Input Format

The first line contains an integer,N , the number of integers in A.
The second line contains N space-separated integers that make up A.

Constraints
1<N<10^3
1<A[i]<10^4

Sample Input 1
4
1 4 3 2
Sample Output 1

2 3 4 1

'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    # Write your code here 
    return a[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
