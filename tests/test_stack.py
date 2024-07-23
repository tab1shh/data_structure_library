import unittest
from data_structures import Stack

class TestStack(unittest.TestCase): # class TestStack that inherits from unittest.TestCase, allowing it to run by unittest
    def test_stack_operation(self): # a test method 
        stack = Stack() # creates an instance of the class 'Stack', so it looks like 'stack = []'
        self.assertTrue(stack.is_empty()) # checks if the 'is_empty()' method of the 'stack' intance return True. 

        # push the number 1, 2, 3 onto the stack
        stack.push(1) # stack = [1]
        stack.push(2) # stack = [1, 2]
        stack.push(3) # stack = [1, 2, 3]

        # checks if the 'size' method of the 'stack' instance returns 3, making sure 3 elements have been added to the stack
        self.assertEqual(stack.size(), 3) # returns 3
        # checks if the 'peek' method of the 'stack' instance return 3, making that the top element of the stack is 3
        self.assertEqual(stack.peek(), 3) # returns 3

        # checks if the 'pop' method of the 'stack' instance return 3, 2, and 1 respectively, making sure the elements are popped off the stack in the correct order
        self.assertEqual(stack.pop(), 3) # returns 3, stack = [1, 2]
        self.assertEqual(stack.pop(), 2) # returns 2, stack = [1]
        self.assertEqual(stack.pop(), 1) # reutrns 1, stack = []

        # checks if the 'is_empty()' method of the 'stack' instance returns True, making sure the stack is empty after being popped
        self.assertTrue(stack.is_empty()) # final state of stack -> 'stack = []'

if __name__ == '__main__':
    unittest.main()

