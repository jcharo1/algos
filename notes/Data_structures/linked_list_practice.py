# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def to_list(self):
#         out = []
#         node = self.head
#         while node:
#             out.append(node.value)
#             node = node.next
#         return out
#     #  Define a function outside of the class
#     def prepend(self, value):
#         """ Prepend a value to the beginning of the list. """
#     # TODO: Write function to prepend here

#         if self.head is None:
#             self.head = Node(value)
#             return
#         new_head = Node(value)
#         new_head.next = self.head
#         self.head = new_head
#     # This is the way to add a function to a class after it has been defined
#     # LinkedList.prepend = prepend
#     def append(self, value):
#         if self.head == None:
#             self.head = Node(value)
        
#         node = self.head
#         while node.next:
#             node = node.next
#         node.next = Node(value)
#     def search(self, value):
#         if self.head is None:
#             return None
#         node = self.head
#         while node:
#             if node.value == value:
#                 return node
#             node = next.node
#         raise ValueError("Value not found in list.")
#     def remove(self, value):
#         if self.head is None:
#             return 
#         if self.head.value == value:
#             self.head = self.head.next 
#             return 
#         node= self.head
#         while node.next:
#             if node.next.value == value:
#                 node.next = node.next.next
#                 return 
#             node = node.next
#         raise ValueError("value not found in list")
#     def pop(self):
#         if self.head is None:
#             return None
#         node = self.head
#         self.head = self.head.next
#         return node.value 
    
#     def insert(self,value,pos):
        
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return

list_with_loop = LinkedList([2, -1, 3, 0, 5])

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next: 
    print(node.value)
    node = node.next   
node.next = loop_start


print(list_with_loop)


def iscircular(linked_list):
    """
    Determine wether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """

    if linked_list.head is None:
        return False
    
    slow = linked_list.head
    fast = linked_list.head
    
    while fast and fast.next:
        # slow pointer moves one node
        slow = slow.next
        # fast pointer moves two nodes
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    # If we get to a node where fast doesn't have a next node or doesn't exist itself, 
    # the list has an end and isn't circular
    return False

print(iscircular(list_with_loop))