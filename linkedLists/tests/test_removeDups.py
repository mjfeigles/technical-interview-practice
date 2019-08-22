"""
Run instructions (for all tests from top directory):
python3 -m unittest discover -s ./linkedLists/tests -v

*tests intended for visual check

Tests solutions to linkedList problems--> prints output for visual check
"""

import unittest
from linkedLists.solutions import removeDups
import random

class TestRemoveDups(unittest.TestCase):
    def test_noDupsOrdered(self):
        head = removeDups.Node(1)
        current = head
        for i in range(5):
            current.next = removeDups.Node(i+2)
            current = current.next
        expected = head
        print()
        print("in: " + '\t' + removeDups.print_linked_list(head))
        removeDups.remove_dups(head)
        print("out: " + '\t' + removeDups.print_linked_list(head))
        self.assertEqual(expected, head)

    def test_emptyList(self):
        head = None
        print()
        print("in: " + '\t' + removeDups.print_linked_list(head))
        removeDups.remove_dups(head)
        print("out: " + '\t' + removeDups.print_linked_list(head))
        self.assertEqual(None, head)

    def test_dupTail(self):
        head = removeDups.Node(0)
        current = head
        for i in range(5):
            current.next = removeDups.Node(i+1)
            current = current.next
        current.next = removeDups.Node(2)
        print()
        print("in: " + '\t' + removeDups.print_linked_list(head))
        removeDups.remove_dups(head)
        print("out: " + '\t' + removeDups.print_linked_list(head))
        # self.assertEqual(solution, head)

    def test_dupHead(self):
        head = removeDups.Node(0)
        current = head
        for i in range(5):
            current.next = removeDups.Node(i)
            current = current.next
        print()
        print("in: " + '\t' + removeDups.print_linked_list(head))
        removeDups.remove_dups(head)
        print("out: " + '\t' + removeDups.print_linked_list(head))
        # self.assertEqual(solution, head)

    def test_dupUnordered(self):
        head = removeDups.Node(0)
        current = head
        for i in range(10):
            current.next = removeDups.Node(random.randint(0, 10)) # int in range [0, 10]
            current = current.next

        print()
        print("in: " + '\t' + removeDups.print_linked_list(head))
        removeDups.remove_dups(head)
        print("out: " + '\t' + removeDups.print_linked_list(head))
        # self.assertEqual(solution, head)

    def test_allRepeats(self):
        head = removeDups.Node(6)
        current = head
        for i in range(10):
            current.next = removeDups.Node(6)
            current = current.next
        print()
        print("in: " + '\t' + removeDups.print_linked_list(head))
        removeDups.remove_dups(head)
        print("out: " + '\t' + removeDups.print_linked_list(head))



if __name__ == "__main__":
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestRemoveDups)
    # testResult = unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()

