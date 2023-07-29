'''
Given a reference to the head of a doubly-linked list and an integer,data ,
create a new DoublyLinkedListNode object having data value data and insert it at the proper location to maintain the sort.

Return a reference to the new list: .

Function Description

Complete the sortedInsert function in the editor below.

sortedInsert has two parameters:

DoublyLinkedListNode pointer head: a reference to the head of a doubly-linked list

int data: An integer denoting the value of the  field for the DoublyLinkedListNode you must insert into the list.

Returns

DoublyLinkedListNode pointer: a reference to the head of the list
Note: Recall that an empty list (i.e., where ) and a list with one element are sorted lists.

Input Format

The first line contains an integerT , the number of test cases.

Each of the test case is in the following format:

The first line contains an integer N, the number of elements in the linked list.
Each of the next  lines contains an integer, the data for each node of the linked list.
The last line contains an integer, data, which needs to be inserted into the sorted doubly-linked list.

Constraints

1<=t<=10
1<=n<=1000

Sample Input

STDIN   Function
-----   --------
1       t = 1
4       n = 4
1       node data values = 1, 3, 4, 10
3
4
10
5       data = 5
Sample Output

1 3 4 5 10
'''

def sortedInsert(llist, data):
    # Write your code here
    data1=DoublyLinkedListNode(data)
    
    if llist.data>data:
        data1.next=llist
        llist.prev=data1
        llist=data1
        return llist
        
    n=llist    
    while n.next!=None:
        if n.next.data>data:
            data1.next=n.next
            data1.prev=n
            n.next.prev=data1
            n.next=data1
            return llist
        n=n.next
        
    if n.next==None:
        n.next=data1
        data1.prev=n
            
    return llist
