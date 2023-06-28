"""
    Reverse String using Stack data structure
"""

from stack import Stack

# function of reverse string
def Reverse_String(stack, input_str):

    # insert input element into stack
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_string = " "

    # pop input element into stack and stored in rev_string varible
    while not stack.is_empty():
        rev_string += stack.pop()
    
    return rev_string

stack = Stack()
input_str = "Hello Python"
print(Reverse_String(stack, input_str))