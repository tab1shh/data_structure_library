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
git clone https://github.com/yourusername/data_structure_library.git
cd data_structure_library
pip install -r requirements.txt
```

## Usage
## Stack
The 'Stack' class provides a stack data structure with 'push', 'pop', 'peek', and 'size' operations.

Example:
```bash
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