"""
    Stack Data-Structure
"""
class Stack():
    # initialized empty list
    def __init__(self):
        self.items = []
        
    # insert element into the stack    
    def push(self, item):
        self.items.append(item)
        
    # Remove last element into the stack    
    def pop(self):
        return self.items.pop()

    # Stack is empty
    def is_empty(self):
        return self.items == []

    # Return top of the stack
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    # Return Stack items    
    def get_stack(self):
        return self.items
    