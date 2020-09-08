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

class LinkedList:
    """
    Data:
    1. A reference to the head Node
    2. A reference to the tail Node

    Behavior/Methods:
    1. Add To Tail 
    2. Prepend (Add a new node and point that Node's next_node at the old Head; update Head pointer)
    3. Remove Head
    4. Remove Tail
    5. Contains?
    6. Get Maximum?
    """

    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    
    def remove_head(self):
        # Empty Linked list
        if self.head is None:
            return None
        ## linkted list only contain one item
        if self.head.get_next() is None:
            head = self.head

            self.head = None

            self.tail = None

            return head.get_value()

        # More than one item
        value = self.head.get_value()
        self.head = self.head.get_next()

        return value

    def remove_tail(self):
        if not self.head:
            return None
        
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        
        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        return value

    def contains(self, value):
        if not self.head:
            return False

        """
        Recursive solution

        def search(node):
            if node.get_value() == value:
                return True
            if not node.get_next():
                return False
            return search(node.get_next())
        return search(self.head)

        get a reference to the node we're currently at;
        update this as we tranverse the list
        """
        current = self.head

        while current:
            #return True if current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            #update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, tehn the target node isn't in our list
        return False

    def get_max(self):
        if not self.head:
            return None
        
        #reference to the largest value we've seen so far
        max_value = self.head.get_value()
        #reference to our current node as we tranverse the list
        current = self.head.get_next()

        while current:
            #check to see if the current value is greater than teh max_value
            if current.get_value() > max_value:
                #if so, updtate our max_value variable
                max_value = current.get_value()
            #update teh current node to the next node int he list
            current = current.get_next()

        return max_value

        
        