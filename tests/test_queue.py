import unittest
from data_structures import Queue

class TestQueue(unittest.TestCase):
    def test_queue_operations(self):
        # new instance of 'Queue' class
        queue = Queue() # queue = []
        # checking if the queue is empty initially
        self.assertTrue(queue.is_empty()) 

        # enqueue the number 1, 2, and 3 respectivley into the queue
        queue.enqueue(1) # queue = [1]
        queue.enqueue(2) # queue = [1, 2]
        queue.enqueue(3) # queue = [1, 2, 3]

        # checks if 'size' method returns 3
        self.assertEqual(queue.size(), 3) # returns 3
        
        # checks if 'dequeue' method returns 1, 2 and 3 respectivley, making sure that elements are dequeued in the correct order
        self.assertEqual(queue.dequeue(), 1) # returns 1, queue = [2, 3]
        self.assertEqual(queue.dequeue(), 2) # returns 2, queue = [3]
        self.assertEqual(queue.dequeue(), 3) # returns 3, queue = []

        # checking if queue is empty after being dequeued 
        self.assertTrue(queue.is_empty()) # queue = []

if __name__ == '__main__':
    unittest.main()