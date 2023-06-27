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
        print(item + " is inserted successfully into the stack")
        
    # Remove last element into the stack    
    def pop(self):
        print(self.items.pop()+ " is poped successfully into the stack")

    # Stack is empty
    def is_empty(self):
        return self.items == []

    # Return top of the stack
    def peek(self):
        if not self.is_empty():
            return "Top of the stack is " + self.items[-1]

    # Return Stack items    
    def get_stack(self):
        return self.items

myStack = Stack()
myStack.push("C")
myStack.push("C++")
myStack.push("Java")
print(myStack.get_stack())
myStack.push("Python")
print(myStack.get_stack())
myStack.pop()
print(myStack.get_stack())
print(myStack.peek())
        
