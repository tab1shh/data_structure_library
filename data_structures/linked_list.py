class Node:
    def __init__(self, data):
        self.data = data # stores data in node
        self.next = None # initialized to none, this will point to the next node in the linked list

class LinkedList:
    def __init__(self): #initalizes a new linked list
        self.head = None # initialized to none, indicating the list is empty
    
    def is_empty(self):
        return self.head is None # returns true if 'head' is none, showing that the list is empty
    
    def append(self, data):
        new_node = Node(data) # a new node is created with the provided data
        if self.is_empty(): # if the linked list is empty
            self.head = new_node # the new node becomes the head of the list
            return
        last = self.head # starts from the head of the list to the find the last node
        while last.next: # loops through the list till it finds the last node
            last = last.next # moves to the next node in the list
        last.next = new_node # links the last node to the new node, making it so it's appending it to the end

    def prepend(self, data): # is used add a new node with 'data' to the beginning of the list
        new_node = Node(data) 
        new_node.next = self.head # points the new nodes 'next' to the current head of the list
        self.head = new_node # updates the head of the list to be the new one

    def delete(self, key): # removes the first occurence of 'key' in the list
        if self.is_empty():
            return 
        temp = self.head # starts from the head of the list, and temp is a node object
        if temp.data == key: # checks if head node has the data we're looking for (which is 'key')
            self.head = temp.next # changes head to the next node
            temp = None # deletes old head node
            return
        while temp is not None: # loops through list to find the node with 'key'
            if temp.data == key: 
                break # if key is found, break
            prev = temp # keeps track of the previous node, so before moving on, remember the current node as 'prev'
            # before moving 'temp' to the next node, 'prev' is assigned the current node 'temp' making it so 'prev' holds the node just before 'temp'
            temp = temp.next # moves 'temp' to the next node, ensuring that 'prev' is one step behind 'temp'
        if temp == None: # if 'key' is not found list, then return
            return
        prev.next = temp.next # links the previous node to the node after the one being deleted
        # so basically, 'prev' will now be linked to 'temp.next' while deleteing 'temp'
        temp = None # deletes node with 'key'

