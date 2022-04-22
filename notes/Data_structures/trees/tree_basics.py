class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value

    def set_left_child(self, node):
        self.left = node
        pass
    def set_right_child(self, node):
        self.right = node
        pass
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right
    
    def has_left_child(self):
        return self.left != None
    def has_right_child(self):
        return self.left != None

node0 = Node()
node0.value = 9

print(f'''
value: {node0.value}
left: {node0.left}
right: {node0.right}
get_value : {node0.get_value()}
'''
)

node0  = Node("apple")
node1 = Node("orange")
node2 = Node("banana")

node0.set_left_child(node1)
node0.set_right_child(node2)


print(f'''

node 0 : {node0.value}
node 0 left child: {node0.left.value}
node 0 right child: {node0.right.value}
node 0 has_left_child : {node0.has_left_child()}
''')