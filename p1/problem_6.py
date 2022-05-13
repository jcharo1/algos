class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        node = self.head
        out_string = ""
        while node:
            out_string += str(node) + " -> "
            node = node.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    if llist_1.head is None:
        return llist_2
    if llist_2.head is None:
        return llist_1
    node = llist_1.head
    list1= []
    list2 = []

    while node:
        list1.append(node.value)
        node = node.next
    node = llist_2.head
    while node:
        list2.append(node.value)
        node = node.next
    union_list = list1 + list2
    
    union_llist = LinkedList()
    for value in union_list:
        union_llist.append(value)


    return union_llist

def get_small_and_large_list(list1,list2):
    if len(list1) < len(list2):
        small = list1
        large = list2
        return small , large
    else:
        small = list2
        large = list1
        return small , large
def intersection(llist_1, llist_2):
    # Your Solution Here
    assert llist_1.head or llist_2.head == None, "Please make sure both Linked List have nodes in them"

    node = llist_1.head
    list1= []
    list2=[]
    list_of_interections=[]
    while node:
        list1.append(node.value)
        node = node.next
    
    node = llist_2.head
    while node:
        list2.append(node.value)
        node = node.next
    
    smaller_list, larger_list = get_small_and_large_list(list1, list2)
    
    for value in larger_list:
        if value in smaller_list:
            list_of_interections.append(value)

    llist_intersections= LinkedList()
    for value in list_of_interections:
        llist_intersections.append(value)
    
    return llist_intersections




# Test case 1
print("-----------Test Case 1-------")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
linked_list_3 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)


print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

print("-----------Test Case 2-------")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))




print("-----------Test Case 3-------")

linked_list_1 = LinkedList()
linked_list_3 = LinkedList()
element_3 = []
element_1 = [3,2,4,35,6,65,6,4,3,21]


for i in element_1:
    linked_list_1.append(i)

for i in element_3:
    linked_list_3.append(i)

print("if AssertionError is raised ----- Test is Passed")
print(intersection(linked_list_3,linked_list_1))

