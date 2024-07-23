import unittest
from data_structures import Queue

class TestQueue(unittest.TestCase):
    def test_queue_operations(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        self.assertEqual(queue.size(), 3)
        
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)

        self.assertTrue(queue.is_empty())

if __name__ == '__main__':
    unittest.main()