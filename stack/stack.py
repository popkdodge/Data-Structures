"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Node:
    """
    Data:
    Store two peice of data:
    1. The Value
    2. The Next Node

    Methods/Behavior/Operations:
    1. Get Value
    2. Set Value
    3. Get Next
    4.Set Next
    """
    def __init__(self, value=None, next_node=None):
        #the value at this linked list Node
        self.value = value
        #reference to the next node in the list
        self.next = next_node

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        #set this node's next_node reference to the passed node
        self.next = new_next

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if len(self.storage) == 0:
            return None
        else:
            return self.storage.pop()
'''
class Stack:
    def __init__(self):
        self.head = None
        
    def push(self, value):
        # if self.head have no value we gonna push a new value
        if self.head is None:
            self.head = Node(value)
        else:
            newhead = Node(value)
            newhead.set_next(self.head)
            self.head = newhead

    def pop(self, value=None):
        if self.head is None:
            return None
        else:
            old = self.head
            self.head = self.head.get_next()
            return old.get_value()
            
    def __len__(self):
        temp = self.head
        count = 0
        while(temp):
            count +=1
            temp=temp.next
        return count
'''