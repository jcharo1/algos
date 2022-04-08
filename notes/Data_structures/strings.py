

# from pickle import TRUE


# just_str = "justin"
# def string_reverser(our_string):

#     """
#     Reverse the input string

#     Args:
#        our_string(string): String to be reversed
#     Returns:
#        string: The reversed string
#     """

#     # New empty string for us to build on
#     new_string = ""

#     # Iterate over old string
#     for i in range(len(our_string)):
#         print(i)
#         # Grab the charecter from the back of the string and add them to the new string
#         new_string += our_string[(len(our_string)-1)-i]
#         print(new_string)
#     # Return our solution
#     return new_string



# def slice_n_reverse_string(string):
#     return string[::-1]

# o ="justin"
# print(slice_n_reverse_string(o))





# str1 = "Udacity"


# # LENGTH
# print(len(str1))		# 7


# # CHANGE CASE
# # The `lower()` and `upper` method returns the string in lower case and upper case respectively
# print(str1.lower())		# udacity
# print(str1.upper())		# UDACITY


# # SLICING
# # string_var[lower_index : upper_index]
# # Note that the upper_index is not inclusive.
# print(str1[1:6]) 		# dacit
# print(str1[:6])			# Udacit. A blank index means "all from that end"
# print(str1[1:])			# dacity

# # A negative index means start slicing from the end-of-string
# print(str1[-6:-1])		# dacit


# # STRIP
# # `strip()` removes any whitespace from the beginning or the end
# str2 = "    Udacity    "
# print(str2.strip())		# Udacity


# # REPLACE/SUBSTITUTE A CHARACTER IN THE STRING
# # The replace() method replaces all occurances a character in a string with another character. The input arguments are case-sensitive
# print(str1.replace('y', "B")) #UdacitB


# # SPLIT INTO SUB-STRINGS
# # The split() method splits a string into substrings based on the separator that we specify as argument
# str3 = "Welcome, Constance!"
# print(str3.split(",")) # ['Welcome', ' Constance!']


# # CONCATENATION
# print(str3 + " " + str1) # Welcome, Constance! Udacity
# marks = 100
# # print(str3 + " You have scored a perfect " + marks) # TypeError: can only concatenate str (not "int") to str
# print(str3 + " You have scored a perfect " + format(marks)) # format() method converts the argument as a formatted string


# # SORT A STRING
# # We can use sorted() method that sort any instance of *iterable*. The characters are compared based on their ascii value
# print(sorted(str3)) # [' ', '!', ',', 'C', 'W', 'a', 'c', 'c', 'e', 'e', 'e', 'l', 'm', 'n', 'n', 'o', 'o', 's', 't']



# print("(---------------------------------------------------------------)")
# j1 ="just  i  n"
# j2 = "us  t n  ji"
# # def anagram_checker(str1, str2):

# #     """
# #     Check if the input strings are anagrams of each other

# #     Args:
# #        str1(string),str2(string): Strings to be checked
# #     Returns:
# #        bool: Indicates whether strings are anagrams
# #     """
    
# #     # TODO: Write your solution here
# #     if sorted(str1.lower()) == sorted(str2.lower()):
# #         return True 
# #     else:
# #         return False


# print(len(j1))
# print(len(j2))



# def anagram_checker(str1, str2):

#     """
#     Check if the input strings are anagrams

#     Args:
#        str1(string),str2(string): Strings to be checked if they are anagrams
#     Returns:
#        bool: If strings are anagrams or not
#     """

#     if len(str1) != len(str2):
#         # Clean strings
#         clean_str_1 = str1.replace(" ", "").lower()
#         clean_str_2 = str2.replace(" ", "").lower()

#         if sorted(clean_str_1) == sorted(clean_str_2):
#             return True

#     return False

# print(anagram_checker(j1,j2))

# t = "justin will go to school"

# print(t.split())





# def word_flipper(our_string):

#     """
#     Flip the individual words in a sentence

#     Args:
#        our_string(string): String with words to flip
#     Returns:
#        string: String with words flipped
#     """
    
#     # TODO: Write your solution here
#     word_list = our_string.split(" ")

#     for idx in range(len(word_list)):
#         word_list[idx] = word_list[idx][::-1]
#     return " ".join(word_list)
# print(word_flipper("hellow my name is justin and i like turtles"))

        
    
# def hamming_distance(str1, str2):

#     """
#     Calculate the hamming distance of the two strings

#     Args:
#        str1(string),str2(string): Strings to be used for finding the hamming distance
#     Returns:
#        int: Hamming Distance
#     """

#     if len(str1) == len(str2):
#         count = 0

#         for char in range(len(str1)):
#             if str1[char] != str2[char]:
#                 count+=1

#         return count

#     return None

# def create_linked_list(input_list):
#     head = None
#     for value in input_list:
#         if head is None:
#             head = Node(value)    
#         else:
#         # Move to the tail (the last node)
#             current_node = head
#             while current_node.next:
#                 current_node = current_node.next
        
#             current_node.next = Node(value)
#     return head


# def create_linked_list_better(input_list):
    
#     head = None
#     tail = None
    
#     for value in input_list:
        
#         if head is None:
#             head = Node(value)
#             tail = head # when we only have 1 node, head and tail refer to the same node
#         else:
#             tail.next = Node(value) # attach the new node to the `next` of tail
#             tail = tail.next # update the tail
            
#     return head




# j = "djskalfjasl;sfjkdsakl;"
# print(j.split())



class LinkedList:
    def __init__(self):
        self.head = None

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

    def to_list(self):
        out_list = []

        node = self.head
        while node:
            out_list.append(node.value)
            node = node.next

        return out_list