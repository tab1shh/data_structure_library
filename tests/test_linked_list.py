import unittest
from data_structures import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_linked_list_operations(self):
        # new instance of 'LinkedList' class
        ll = LinkedList() # ll = []
        # checking if linked list is empty
        self.assertTrue(ll.is_empty())

        # appends 1, 2, and 3 respectivley to the linked list
        ll.append(1) # ll = [1]
        ll.append(2) # ll = [1, 2]
        ll.append(3) # ll = [1, 2, 3]

        # checkf if the 'search' method of 'll' instance returns true for 2 (in the list) and false for 4 (not in the list)
        self.assertEqual(ll.search(2), True) # returns True
        self.assertEqual(ll.search(4), False) # returns False

        # deletes 2 from linked list, and checks if 2 is in the linked verifying that it was deleted
        ll.delete(2) # ll = [1, 3]
        self.assertEqual(ll.search(2), False) # returns False

        # prepend 0 to the linked list and check if 'data' attribute of the 'head' node of the linked list is 0, verifying that 0 is prepended to the list
        ll.prepend(0) # ll = [0, 1, 3]
        self.assertEqual(ll.head.data, 0) # returns 0

if __name__ == '__main__':
    unittest.main()
