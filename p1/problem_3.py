import heapq
import sys

class Node():
    def __init__(self, frequency):
        self.value = None
        self.frequency = frequency
        self.left = None
        self.right = None

    def set_left(self,left_value):
        self.left = left_value

    def set_right(self, right_value):
        self.right = right_value
    
    def set_value(self,value):
        self.value = value
    
    def get_value(self):
        return self.value
    
    def get_frequency(self):
        return self.frequency

    def interior(self):
        return self.value is None

    def __repr__(self):
        return "Node(freq: {}, value: {})".format(self.get_frequency(),self.get_value())
    
    def __lt__(self, other):
        return self.get_frequency() < other.get_frequency()

class Tree(object):

    def __init__(self,value):
        self.root = Node(value)


    def get_root(self):
        return self.root

def frequency_dict_builder(string):
    frequency_dict={}
    for char in string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict



def tree_to_binary_code(root):
    
    codes_dict = {}
    bits = ''

    def traverse(root,bits):

        if not root.interior():
            codes_dict[root.value] = bits
        else:
            if root.left != None:
                traverse(root.left, bits+'0')
            if root.right!= None:
                traverse(root.right, bits +"1")
    
    traverse(root,bits)
    return codes_dict

def huffman_encoding(data):
    assert isinstance(data, str)
    assert len(data)>0
    ##obatain frequency
    frequency_dict = frequency_dict_builder(data)
    #create heap
    heap = []
    for char, frequency in frequency_dict.items():

        node = Node(frequency)
        node.set_value(char)
        heapq.heappush(heap, node)
    
    
    while len(heap) > 1:
        
        min = heapq.heappop(heap)
        next_min = heapq.heappop(heap)
        
        internal_node = Node(min.get_frequency()+next_min.get_frequency())
        internal_node.set_left(min)
        internal_node.set_right(next_min)

        heapq.heappush(heap, internal_node)
    
    tree = heap[0]
    if not heap[0].interior():
        
        interior_node = Node(heap[0].get_frequency())
        interior_node.set_left(heap[0])
        interior_node.set_right(Node(None))
        tree = interior_node
      

    letters_to_binary = tree_to_binary_code(tree)
    encoded_messeage = ""
    for letter in data:
        encoded_messeage += letters_to_binary[letter]
    
    return encoded_messeage, tree

def huffman_decoding(encoded_data, tree):
    'Decode data using huffman tree'

    node = tree
    decoded_data = ''
    index = 0
    while index < len(encoded_data):
        
        if encoded_data[index] == '0':
            node = node.left
        else:
            node = node.right

        if not node.interior():
            decoded_data += node.get_value()
            node = tree
        
        index += 1
        
    return decoded_data

print(huffman_encoding("AAAAAAABBBCCCCCCCDDEEEEEE"))
encoded_data, tree = huffman_encoding("AAAAAAABBBCCCCCCCDDEEEEEE")
print(huffman_decoding(encoded_data, tree))

if __name__ == "main":
    code = {}
    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))