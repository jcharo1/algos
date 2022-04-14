"""
Problem Statement
Given a linked list with integer data, arrange the elements in such a manner that all nodes with even numbers are placed after odd numbers. Do not create any new nodes and avoid using any other data structure. The relative order of even and odd elements must not change.

Example:

linked list = 1 2 3 4 5 6
output = 1 3 5 2 4 6

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    if head is None:
        return head

    even_head = None
    even_tail= None

    odd_head = None
    odd_tail  = None

    current = head 
    while current:
        next_node = current.next
        
        if current.data % 2 == 0:

            if even_head is None:
                even_head = current
                even_tail = even_head
            else:
                even_tail.next= current
                even_tail = even_tail.next
        else:
            if odd_head is None:
                odd_head = current 
                odd_tail = odd_head
            else:
                odd_tail.next = current
                odd_tail = odd_tail.next
        current.next = None
        current = next_node
    if odd_head is None:
        return even_head
    odd_tail.next = even_head

    return odd_head