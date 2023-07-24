'''
There is a collection of input strings and a collection of query strings. For each query string,
determine how many times it occurs in the list of input strings. Return an array of the results.

Example
strings=['ab','ab','abc']
queries=['ab','abc','bc']


There are  instances 2 of 'ab', 1 of 'abc' and 0 of 'bc'. For each query, add an element to the return array, .

Function Description

Complete the function matchingStrings in the editor below. 
The function must return an array of integers representing the frequency of occurrence of each query string in stringList.

matchingStrings has the following parameters:

string stringList[n] - an array of strings to search
string queries[q] - an array of query strings

Returns
int[q]: an array of results for each query

Input Format

The first line contains and integer N, the size of Strings.
Each of the next N lines contains a string .
The next line contains M, the size of queries.
Each of the next M lines contains a string .

Constraints

0<N,M,<=1000

Sample Input 1 
4
aba
baba
aba
xzxb
3
aba
xzxb
ab

Sample Output 1

2
1
0
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries
#

def matchingStrings(stringList, queries):
    # Write your code here
    results=[stringList.count(x) for x in queries]
    print(results)
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stringList_count = int(input().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
