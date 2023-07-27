'''
Given a pointer to the head of a linked list and a specific position, determine the data value at that position.
Count backwards from the tail node. The tail is at postion 0, its parent is at 1 and so on.


Each of the data values matches its distance from the tail. The value data is at the desired position.

Function Description

Complete the getNode function in the editor below.

getNode has the following parameters:

SinglyLinkedListNode pointer head: refers to the head of the list
int positionFromTail: the item to retrieve

Returns
int: the value at the desired position

Input Format
The first line contains an integer T , the number of test cases.

Each test case has the following format:
The first line contains an integer N, the number of elements in the linked list.
The next  lines contains an integer, the data value for an element of the linked list.
The last line contains an integer M , the position from the tail to retrieve the value of.

Constraints
0<=N,M,listi <=1000
listi, where  is the  element of the linked list.
Sample Input

2
1
1
0
3
3
2
1
2
Sample Output

1
3
'''
#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'getNode' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER positionFromTail
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def getNode(llist, positionFromTail):
    # Write your code here
    prev=None
    nxt=None
    while llist!=None:
        nxt=llist.next
        llist.next=prev
        prev=llist
        llist=nxt
    
    while positionFromTail>0:
        prev=prev.next
        positionFromTail-=1
    return prev.data

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        position = int(input())

        result = getNode(llist.head, position)

        fptr.write(str(result) + '\n')

    fptr.close()
