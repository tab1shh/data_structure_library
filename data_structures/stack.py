class Stack:
    def __init__(self):
        self.items = [] # initalizes an empty list named 'items' to store elements in the stack 

    def is_empty(self):
        return len(self.items) == 0 # returns true if the stack is empty
    
    def push(self, item):
        self.items.append(item) # appends 'item' to the end of the list named 'items'

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
        # if stack is not empty then remove item at the top of the stack, otherwise do nothing
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
        # if stack is not empty return the last from the list (top of the stack) without removing it
    
    def size(self):
        return len(self.items) # return the size of the stack
