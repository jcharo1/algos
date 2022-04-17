from sqlalchemy import values


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class Stack:
    
    def __init__(self):
        self.head = None # No items in the stack, so head should be None
        self.num_elements = 0 # No items in the stack, so num_elements should be 0
    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            new_node = self.head
        self.num_elements += 1
    def size(self):
        return self.num_elements
    def is_empty(self):
        return self.num_elements == 0
    def pop(self):
        value = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return value



foo = Stack()
foo.push(3)
print(foo.is_empty())

