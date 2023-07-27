'''
A linked list is said to contain a cycle if any node is visited more than once while traversing the list.
Given a pointer to the head of a linked list, determine if it contains a cycle. If it does, return 1. Otherwise, return 0.

Function Description

Complete the has_cycle function in the editor below.

It has the following parameter:

SinglyLinkedListNode pointer head: a reference to the head of the list

Returns
int:  if there is a cycle or  if there is not
Note: If the list is empty,  will be null.

Input Format
The code stub reads from stdin and passes the appropriate argument to your function.
The custom test cases format will not be described for this question due to its complexity
. Expand the section for the main function and review the code if you would like to figure out how to create a custom case.

Constraints
0 <= list size <=1000

Sample Output

0
1
Explanation

The first list has no cycle, so return 0.
The second list has a cycle, so return 1.
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

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    visited = set()
    f = head
    while f:
        i = id(f)
        print(i)
        if i in visited:
            return 1
        visited.add(i)
        f = f.next
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        extra = SinglyLinkedListNode(-1);
        temp = llist.head;

        for i in range(llist_count):
            if i == index:
                extra = temp

            if i != llist_count-1:
                temp = temp.next

        temp.next = extra

        result = has_cycle(llist.head)

        fptr.write(str(int(result)) + '\n')

    fptr.close()
