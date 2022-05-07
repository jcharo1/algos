'''DFS-------PRE-ORDER TRAVERSAL'''

'''
START AT THE ROOT ----- VISIT IT 
CHECK IF THERES A LEFT CHILD WE GO DOWN TO THE LEFT CHILD ---- VISIT IT 
CHECK IF THERES A LEFT CHILD IF SO WELL----------- VISIT IT
CHECK IF THERE IS A LEFT CHILD IF NOT -------- CHECK IF THERE IS A RIGHT CHILD --- IF NOT GO BACK UP 

CHECK IF THERE IS A RIGHT CHILD IF NOT GO BACK UP 
CHECK IF THERE IS A RIGHT CHILD 




'''
'''
Traverse a tree (depth first search)
Traversing a tree means "visiting" all the nodes in the tree once. Unlike an array or linked list, there's more than one way to walk through a tree, starting from the root node.

Traversing a tree is helpful for printing out all the values stored in the tree, as well as searching for a value in a tree, inserting into or deleting values from the tree. There's depth first search and breadth first search.

Depth first search has 3 types: pre-order, in-order, and post-order.

Let's walk through pre-order traversal by hand first, and then try it out in code.
'''

# this code makes the tree that we'll traverse

class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
    
    # set value of the node
    def set_value(self,value):
        self.value = value
    
    # get value of the node
    def get_value(self):
        return self.value
    
    # set a node for the left child
    def set_left_child(self,left):
        self.left = left
    
    # set a node for the right child
    def set_right_child(self, right):
        self.right = right
    
    # get the node of left child
    def get_left_child(self):
        return self.left
    
    # get the node of right child
    def get_right_child(self):
        return self.right

    # check if node has left child -> return boolean
    def has_left_child(self):
        return self.left != None
    
    # check if node has right child -> return boolean
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
    
    
class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root


tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

# Let's define a stack to help keep track of the tree nodes
# class Stack():
#     def __init__(self):
#         self.list = list()
    
#     # add an element to the list
#     def push(self,value):
#         self.list.append(value)
        
#     # remove the last element from the list
#     def pop(self):
#         return self.list.pop()
        
#     # get the value of the last element in the list
#     def top(self):
#         if len(self.list) > 0:
#             return self.list[-1]
#         else:
#             return None
    
#     # check if the list empty
#     def is_empty(self):
#         return len(self.list) == 0
    
#     # 
#     def __repr__(self):
#         if len(self.list) > 0:
#             s = "<top of stack>\n_________________\n"
#             s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
#             s += "\n_________________\n<bottom of stack>"
#             return s
        
#         else:
#             return "<stack is empty>"



# def pre_order_with_stack(tree, debug_mode=False):
#     visit_order = list()
#     stack = Stack()
#     node = tree.get_root()
#     visit_order.append(node.get_value())
#     state = State(node)
#     stack.push(state)
#     count = 0
#     while(node):
#         if debug_mode:
#             print(f"""
# loop count: {count}
# current node: {node}
# stack:
# {stack}
#             """)
#         count +=1
#         if node.has_left_child() and not state.get_visited_left():
#             state.set_visited_left()
#             node = node.get_left_child()
#             visit_order.append(node.get_value())
#             state = State(node)
#             stack.push(state)

#         elif node.has_right_child() and not state.get_visited_right():
#             state.set_visited_right()
#             node = node.get_right_child()
#             visit_order.append(node.get_value())
#             state = State(node)

#         else:
#             stack.pop()
#             if not stack.is_empty():
#                 state = stack.top()
#                 node = state.get_node()
#             else:
#                 node = None
            
#     if debug_mode:
#             print(f"""
# loop count: {count}
# current node: {node}
# stack:
# {stack}
#             """)
#     return visit_order



def pre_order(tree):
    visit_order = []

    root = tree.get_root()
    traverse(root)

    def traverse(node):
        if node:

            #visit 
            visit_order.append(node.get_value())
            #traverse left
            traverse(node.get_left_child())
            #traverse right
            traverse(node.get_right_child())
    
    traverse(root)
    return visit_order