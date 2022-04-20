
"""
Keypad Combinations
A keypad on a cellphone has alphabets for all numbers between 2 and 9, as shown in the figure below:

A cell phone keypad that has letters associated with each number 2 through 9

You can make different combinations of alphabets by pressing the numbers.

For example, if you press 23, the following combinations are possible:

ad, ae, af, bd, be, bf, cd, ce, cf

Note that because 2 is pressed before 3, the first letter is always an alphabet on the number 2. Likewise, if the user types 32, the order would be

da, db, dc, ea, eb, ec, fa, fb, fc

Given an integer num, find out all the possible strings that can be made using digits of input num. Return these strings in a list. The order of strings in the list does not matter. However, as stated earlier, the order of letters in a particular string matters."""



def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""

def keypad(num):
    
    # TODO: Write your keypad solution here!
    if num <= 1:
        return [""]
    
    
    elif 1 < num <=9:
        return list(get_characters(num))

    last_digit = num % 10 

    small_output = keypad(num//10)

    keypad_string = get_characters(last_digit)

    output= []

    for charc in keypad_string:
        for item in small_output:
            new_item = item + charc
            output.append(new_item)
    return output
    
