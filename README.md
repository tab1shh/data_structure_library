# data_structure_library

This projects aims to implement a custom data structure libaray in python to help understand common data structures. The library includes implementations of Stacks, Queues, and Linked Lists.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Stack](#stack)
  - [Queue](#queue)
  - [Linked List](#linked-list)
- [Running Tests](#running-tests)

## Installation

Clone the repository and install dependencies (if any).
```bash
git clone https://github.com/tab1shh/data_structure_library
cd data_structure_library
pip install -r requirements.txt
```

## Usage
### Stack
The 'Stack' class provides a stack data structure with 'push', 'pop', 'peek', and 'size' operations.

Example:
```python
from data_structures.stack import Stack

# Create a new stack
stack = Stack()

# Push items onto the stack
stack.push(1)
stack.push(2)

# Check the top item
print(stack.peek())  # Output: 2

# Pop an item from the stack
print(stack.pop())   # Output: 2

# Check if the stack is empty
print(stack.is_empty())  # Output: False

# Get the size of the stack
print(stack.size())  # Output: 1
```

### Queue
The 'Queue' class provides a queue data structure with 'enqueue', 'dequeue', and 'size' operations.
Example:
```python
from data_structures.queue import Queue

# Create a new queue
queue = Queue()

# Enqueue items
queue.enqueue(1)
queue.enqueue(2)

# Dequeue an item
print(queue.dequeue())  # Output: 1

# Check if the queue is empty
print(queue.is_empty())  # Output: False

# Get the size of the queue
print(queue.size())  # Output: 1
```

### Linked List
The 'LinkedList' class provides a linked list data structure with 'append', 'prepend', 'delete', and 'search' operations
Example:
```python
from data_structures.linked_list import LinkedList

# Create a new linked list
ll = LinkedList()

# Append items
ll.append(1)
ll.append(2)

# Display the linked list
ll.display()  # Output: 1 -> 2

# Prepend an item
ll.prepend(0)

# Display the linked list again
ll.display()  # Output: 0 -> 1 -> 2

# Search for an item
print(ll.search(1))  # Output: True
print(ll.search(3))  # Output: False

# Delete an item
ll.delete(1)
ll.display()  # Output: 0 -> 2
```

## Running Tests
Run the test suite using 'unittest' or 'pytest'.

Using 'unittest'
```bash
python -m unittest discover tests
```

Using 'pytest'
```bash
pytest
```
