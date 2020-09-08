"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
'''
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        pop(self.storage)

'''
from singly_linked_list import Node
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            new.set_next(self.head)
            self.head = new
    def dequeue(self):
        if self.head is None:
            return None
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        else:
            current = self.head
            next =  current.get_next()
            while next is not self.tail:
                current = current.get_next()
                next = next.get_next()

            self.tail = current
            self.tail.set_next(None)
            return next.get_value()

    def __len__(self):
        temp = self.head
        count = 0
        while(temp):
            count +=1
            temp=temp.next
        return count
    