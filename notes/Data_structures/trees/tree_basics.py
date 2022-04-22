class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
    def get_value(self):
        return self.value

node0 = Node()
node0.value = 9
print(f'''
value: {node0.value}
left: {node0.left}
right: {node0.right}
'''
)
