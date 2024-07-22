class Queue:
    def __init__(self):
        self.items = [] # initalizes an empty list named 'items' to store elements in the stack 

    def is_empty(self):
        return len(self.items) == 0 # returns true if the stack is empty
    
    def enqueue(self, item):
        self.items.insert(0, item) # inserts item to the beginning of 'items' (0)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        return None
     # if list is not empty, then pop the top element
    
    def size(self):
        return len(self.items) # return the size of the list