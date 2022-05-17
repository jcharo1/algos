import hashlib

from datetime import datetime, timezone



class Block:

    def __init__(self, data, previous_hash):
      self.timestamp = datetime.now(timezone.utc)
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
    

    def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = (str(self.data) + str(self.previous_hash)+ str(self.timestamp)).encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

    def get_previous_hash(self):
        return self.previous_hash
    
    def get_hash(self):
        return self.hash
    def __str__(self):
        """
        String representation of the block.
        """
        s = "Block:\n"
        s += "Timestamp: " + str(self.timestamp) + "\n"
        s += "Data: " + str(self.data) + "\n"
        s += "Hash: " + str(self.hash) + "\n"
        return s
    




class Block_chain:



    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, data):
        if type(data) != str:
            return print("Please ensure data is a string")
        if len(data) == 0:
            return print("please ensure your string is not empty")
        if self.head is None:
            self.head = Block(data, 0)
            self.tail = self.head

        
        else:
            new_block = Block(data, self.tail.get_hash)

            self.tail = new_block
        self.size += 1
    def get_size(self):
        return self.size



print("-----------Test Case 1-------")
block_chain = Block_chain()

block_chain.append("J")
block_chain.append("M")
block_chain.append("C")
block_chain.append("M")

print(block_chain.head)

print(block_chain.get_size())
print("Test case 1, returns prints 4 as the size of the block chain")


print("-----------Test Case 2-------")

block_chain2 = Block_chain()

block_chain2.append("J")
block_chain2.append(35)

print("Test case 2, return Please ensure data is a string")


print("-----------Test Case 3-------")

block_chain = Block_chain()

block_chain.append("J")
block_chain.append(None)
print("Test case 3, returns  if data is not of string type since None is not a string error will occur")



print("--------------------Test case 4------------------")
block_chain1 = Block_chain()
block_chain1.append("") 
print("Test case 4, returns  please ensure your string is not empty")



