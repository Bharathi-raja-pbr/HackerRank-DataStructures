# Data Structures

      1)Array
      2)linked list
      3)Stack
      4)Queue
      5)Binary trees
      6)BST
      7)Graphs
      8)Hashmap


# Array
                    An array is a type of data structure that stores elements of the same type in a contiguous block of memory.
        In an array, arr, of size ,N each memory location has some unique index, i (where 0<=i<len(arr), that can be referenced as 
        arr[i]  or ai.

 # Initialisation
#         --> Empty array
               A=[]
        
#         --> Array with null values of length n
         A=[0]*n
        
         can be done for any values.
        
 #       --> Initialise array with input from user in single line
         A=list(map(int,input().rstrip().split()))
        
         to get an integer array rstrip-to remove spaces following ; split-tosplit the input in single line based on separator
        
 #        --> Iniatialise array in a range
         A=[x for x in range(start,stop)] # List comprehension

#         --> 2-D array:
         A=[[] for i in range(3)] 

# Add elements to array

       --> Add at the end
       arr=[1,2,3]
       arr.append(4)
       print(arr)
       o/p: [1,2,3,4]
      
       --> Insert at a specific index
       arr.insert(1,5)
       print(arr)
       o/p: [1,5,2,3,4]

# Reverse of an array
      
        arr=[1,2,3]
        arr[::-1] 
        o/p=[3,2,1]

 # Accessing elements:
      arr=[1,2,3]
      arr[0]=1
      arr[1]=2
      arr[2]=3

#      Negative indexing
      arr[-1]=3
      arr[-2]=2
      arr[-3]=1

# Functions on array

# len()
       Returns the length of the array
       arr=[1,2,3]
       print(len(arr))
       o/p: 3

# sum()
        Returns the sum of the array
        print(sum(arr))
        o/p: 6

# index()
        Returns the index of element if found. Else returns -1
        print(arr.index(2))
        o/p:1
        print(arr.index(4))
        o/p:-1

# Rotating the array:

#       --> Left Rotation

      A left rotation operation on an array of size N shifts each of the array's elements 1 unit to the left. Given an integer,D ,
      rotate the array that many steps left and return the result.
      Method1:
      def rotateLeft(d, arr):
          # Write your code here
          val=[]
          n=len(arr)
          d=d%n
          
          for i in range(0,n):
              val.append(arr[(i+d)%n])
          return val
      Method2:
      def rotate(self, nums: List[int], k: int) -> None:
              temp = []
              k = len(nums) - k  # Calculate the left rotation steps
              if k >= len(nums):
                  k = k % len(nums)
              temp = nums[:k]
              nums[:len(nums)-k] = nums[k:]
              nums[len(nums)-k:] = temp

#        --> Right Rotation

      A right rotation operation on an array of size N shifts each of the array's elements 1 unit to the right. Given an integer,D ,
      rotate the array that many steps right and return the result.
      
            Method1:
            def rotateRight(d, arr):
                # Write your code here
                val=[]
                n=len(arr)
                d=d%n
                
                for i in range(0,n):
                    val.append(arr[(n-d+i)%n])
                return val

          Method2:
          def rotate(self, nums: List[int], k: int) -> None:
              temp= []
              if k >= len(nums):
                  k = k % len(nums)
              temp = nums[-k:]
              print(nums[-k:])
              print(nums[:-k])
              nums[k:] = nums[:-k]
              nums[:k] = temp

# Remove Duplicates 

    Allows only one occurence of elements
    Approach: Move unique elements to the left and return the first half with unique elements
    
     def removeDuplicates(self, nums: List[int]) -> int:
            '''if len(nums) == 0:
                return 0   # use in case if constraint on len(nums) starts from 0'''

            i = 1
            for j in range(1, len(nums)):
                if nums[j] != nums[j-1]:
                    nums[i] = nums[j]
                    i += 1

            return nums[:i]

    Allows K repeatation of elements 

    def removeDuplicates(self, nums: List[int], limit: int) -> int:
        if len(nums) <= limit:
            return len(nums)

        i = limit
        while i < len(nums):
            duplicate = True
            for j in range(1, limit + 1):
                if nums[i] != nums[i - j]:
                    duplicate = False
                    break

            if duplicate:
                nums.pop(i)
            else:
                i += 1

        return nums

# Merge Arrays

      list1,list2 can be combined using
      
      --> using extend()
      list1.extend(list2)
      
      --> using + operator
      list1+list2

# Sort Arrays

      -->Ascending order
      arr=[1,2,3]
      arr.sort()
      
      -->Descending order
      arr.sort(reverse=True)


# LINKED LIST

#            Types:
                  1)Singly linked list
                  2)Doubly linked list
                  3)Circular linked list

# Singly Linked List

      A Singly linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.
      It has two components:
      1)Data
      2)Next - pointer to next data

      Structure:
                    -------------           -------------
          HEAD---> | DATA | NEXT | ---->   | DATA | NEXT | --->TAIL
                    -------------           -------------

# Advantages of Linked list:
      Dynamic Data Structure
      No Memory Wastage
      Implementation
      Faster Insertion and Deletion Operation
      Memory Usage is Efficient
      Random Access
      Reverse Traversal

# Operations on linked list
       1)Insert
       2)Delete
       3)Traversal

#  --> INSERT:

        1)insert at beginning
        2)insert at end
        3)insert before an element
        4)insert after an element
        
#  --> DELETE:

        1)delete at beginning
        2)delete at end
        3)delete before an element
        4)delete after an element

#    LinkedList declaration from scratch in python
      class node:
        def __init__(self,data=None):
          self.data=data
          self.next=None
      
      class linked:
        def __init__(self):
          self.head=None
      
        def show(self):
          node=self.head
          while node is not None:
           print(node.data,sep=' ')
           node=node.next
      
        def add_begin(self,data):
          new_node=node(data)
          new_node.next=self.head
          self.head=new_node
          
        def add_end(self,data):
          new_node=node(data)
          #if the linked list is empty 
          if self.head is None:
              self.head=new_node
          #if linked list is not empty
          else:
              n=self.head
              while n.next is not None: 
                  n=n.next
              n.next=new_node
              
        def add_after(self,data,x):
            new_node=node(data)
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.next
            #if search element is not found in the linked list
            if n is None:
                print("node not found")
                return 0
            #if found 
            temp=n.next
            n.next=new_node
            new_node.next=temp
            
            
        def add_before(self,data,x):
            new_node=node(data)
            #if linked list is empty
            if self.head is None:
                print("empty")
                return
            #if the first element is the search element
            if self.head.data==x:
                new_node.next=self.head
                self.head=new_node
                return
            #else
            n=self.head
            while n.next is not None:
                if n.next.data==x:
                    break
                n=n.next
            #if element is not found
            if n.next is None:
                print("not found")
                return
            new_node.next=n.next
            n.next=new_node
            
        def delete_begin(self):
            if self.head is None:
                print("empty")
                return
            
            self.head=self.head.next
            
        def delete_end(self):
            n=self.head
            if n is None:
                print("empty")
                return
            elif self.head.next==None:
                self.head=None
            else: 
             while n.next.next is not None:
                n=n.next
             n.next=None


# Breaking the code 

#    Creating Node class
      class node:
        def __init__(self,data=None):
          self.data=data
          self.next=None
#    Creating Linked List class  
      class linked:
        def __init__(self):
          self.head=None
#      Print elements
        def show(self):
          node=self.head
          while node is not None:
           print(node.data,sep=' ')
           node=node.next
  #    Insert elements
  #    Insert @ Beginning 
        def add_begin(self,data):
          new_node=node(data)
          new_node.next=self.head
          self.head=new_node
  #    Insert @  End      
        def add_end(self,data):
          new_node=node(data)
          #if the linked list is empty 
          if self.head is None:
              self.head=new_node
          #if linked list is not empty
          else:
              n=self.head
              while n.next is not None: 
                  n=n.next
              n.next=new_node
  #    Insert @   After a given element       
        def add_after(self,data,x):
            new_node=node(data)
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.next
            #if search element is not found in the linked list
            if n is None:
                print("node not found")
                return 0
            #if found 
            temp=n.next
            n.next=new_node
            new_node.next=temp
            
  #    Insert @  Before a given element     
        def add_before(self,data,x):
            new_node=node(data)
            #if linked list is empty
            if self.head is None:
                print("empty")
                return
            #if the first element is the search element
            if self.head.data==x:
                new_node.next=self.head
                self.head=new_node
                return
            #else
            n=self.head
            while n.next is not None:
                if n.next.data==x:
                    break
                n=n.next
            #if element is not found
            if n.next is None:
                print("not found")
                return
            new_node.next=n.next
            n.next=new_node

#       Insert at a specified Position
            def insertNodeAtPosition(llist, data, position):
                # Write your code here
                node=SinglyLinkedListNode(data)
                if position == 0:
                    
                    node.next=llist
                    llist=node
                n=llist
                while position>1:
                    n=n.next
                    position-=1
                node.next=n.next
                n.next=node
                
                return llist
      
#        Delete elements  
#        Delete @  Beginning
        def delete_begin(self):
            if self.head is None:
                print("empty")
                return
            
            self.head=self.head.next
#        Delete @    End       
        def delete_end(self):
            n=self.head
            if n is None:
                print("empty")
                return
            elif self.head.next==None:
                self.head=None
            else: 
             while n.next.next is not None:
                n=n.next
             n.next=None

#         Delete a given element

          def delete_element(self,x):
              if self.head is None:
                  print("linked list is empty")
              if self.head.data==x:
                  self.head=self.head.next
                  return
              n=self.head
              while n.next is not None:
                  if n.next.data==x:
                      break
                  n=n.next
              if n.next is None:
                  print("element not found")
              else:
                  n.next=n.next.next


#         Delete a element at given position

            def deleteNode(llist, position):
                # Write your code here
                if position==0:
                    llist=llist.next
                    return llist
                n=llist
                while position>1:
                    n=n.next
                    position-=1
                n.next=n.next.next
            
#         Reverse a Linked List

            def reverse(self):
                    prev=None
                    cur=self.head
                    nxt=None
                    
                    while cur is not None:
                        nxt=cur.next
                        cur.next=prev
                        prev=cur
                        cur=nxt
                    self.head=prev

# Doubly Linked List

      A Doubly linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.
            It has three components:
            1)Data
            2)Next - pointer to next data
            3)Prev - pointer to previous data
      
            Structure:
                        ---------------------            -------------------
                None<---| PREV | DATA | NEXT |   ---->   |PREV| DATA | NEXT | --->None
                        ---------------------    <----   -------------------
                               (HEAD)                         (TAIL)

#  Code from scratch
      class Node:
        def __init__(self,data):
          self.data=data
          self.nref=None
          self.pref=None
      
      class DLL:
        def __init__(self):
            self.head=None
# print from head to tail
        def show_forward(self):
          if self.head==None:
            print("empty")
            return
          n=self.head
          while n!=None:
            print(n.data,end=' ')
            n=n.nref
          print('\n--------')
# print from tail to head
        def show_reverse(self):
          if self.head==None:
            print("empty")
            return
          n=self.head
          while n.nref!=None:
            n=n.nref
          while n!=None:
            print(n.data,end=' ')
            n=n.pref
          print('\n--------')
# Insert at Beginning
        def insert_begin(self,data):
          new_node=Node(data)
          if self.head==None:
            self.head=new_node
            return
          new_node.nref=self.head
          self.head.pref=new_node
          self.head=new_node
# Insert at End
        def insert_end(self,data):
          new_node=Node(data)
          if self.head==None:
            self.head=new_node
            return
          n=self.head
          while n.nref!=None:
            n=n.nref
          new_node.pref=n
          n.nref=new_node
# Insert before a given element
        def insert_before(self,data,value):
          # if list is empty
          if self.head==None:
            print("empty list")
            return
          new_node=Node(data)
          # if head.data is the value given
          if self.head.data==value:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
            return
          #else
          n=self.head
          while n.nref!=None:
            if n.nref.data== value:
               break
            n=n.nref
          #the loop breaks in case the element is not found in the list 
          if n.nref==None:
            print("element not found")
          else:
            #print(n.nref.data)
            new_node.nref=n.nref
            n.nref=new_node
            new_node.pref=n
# Insert after a given element
        def insert_after(self,data,value):
          #if list is empty
           if self.head==None:
            print("list empty")
            return
      
           new_node=Node(data)
           #if head.data is the value given
           if self.head.data==value:
             n=self.head.nref
             new_node.nref=n
             n.pref=new_node
             new_node.pref=self.head
             self.head.nref=new_node
             return
           
           #else
           n=self.head
           while n!=None:
            if n.data==value:
              break
            n=n.nref
           if n==None:
            print("element not found")
           else:
            new_node.nref=n.nref
            new_node.pref=n
            n.nref=new_node
      
      
      ll=DLL()
      ll1=DLL()
      ll.insert_begin(20)
      ll.insert_begin(10)
      ll.insert_end(30)
      ll.show_forward()
      #ll1.show_reverse()
      ll.show_reverse()
      ll.insert_before(25,10)
      ll.insert_after(100,30)
      ll.show_forward()


