class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out
    #  Define a function outside of the class
    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
    # TODO: Write function to prepend here

        if self.head is None:
            self.head = Node(value)
            return
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
    # This is the way to add a function to a class after it has been defined
    # LinkedList.prepend = prepend
    def append(self, value):
        if self.head == None:
            self.head = Node(value)
        
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
    def search(self, value):
        if self.head is None:
            return None
        node = self.head
        while node:
            if node.value == value:
                return node
            node = next.node
        raise ValueError("Value not found in list.")
    def remove(self, value):
        if self.head is None:
            return 
        if self.head.value == value:
            self.head = self.head.next 
            return 
        node= self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return 
            node = node.next
        raise ValueError("value not found in list")
    def pop(self):
        if self.head is None:
            return None
        node = self.head
        self.head = self.head.next
        return node.value 
    
    def insert(self,value,pos):
        

        