"""
Run instructions (for all tests from top directory):
python3 -m unittest discover -s ./linkedLists/tests -v

*tests intended for visual check

Tests solutions to linkedList problems--> prints output for visual check
"""

import unittest
from linkedLists.solutions import partition
import random

class TestPartition(unittest.TestCase):

    def test_tenNodesUnordered(self):
        head = partition.Node(0)
        current = head
        for i in range(10):
            current.next = partition.Node(random.randint(0, 10)) # int in range [0, 10]
            current = current.next

        print()
        k = random.randint(0, 10)
        print("in: " + '\t' + partition.print_linked_list(head) + " k-value: " + str(k))
        head = partition.partition(head, k)
        print("out: " + '\t' + partition.print_linked_list(head))
        # self.assertEqual(solution, head)

    def test_oneNode(self):
        head = partition.Node(6)
        print()
        k = 1
        print("in: " + '\t' + partition.print_linked_list(head) + " k-value: " + str(k))
        head = partition.partition(head, k)
        print("out: " + '\t' + partition.print_linked_list(head))

    def test_None(self):
        print()
        print("in: " + '\t' + "None" + " k-value: " + str(1))
        output = partition.partition(None, 1)
        print("out: " + '\t' + partition.print_linked_list(output))

    def test_twentyNodes(self):
        head = partition.Node(0)
        current = head
        for i in range(20):
            current.next = partition.Node(random.randint(0, 100)) # int in range [0, 100]
            current = current.next
        print()
        k = random.randint(0, 10)
        print("in: " + '\t' + partition.print_linked_list(head) + " k-value: " + str(k))
        head = partition.partition(head, k)
        print("out: " + '\t' + partition.print_linked_list(head))

    def test_orderedList(self):
        head = partition.Node(0)
        current = head
        for i in range(10):
            current.next = partition.Node(i)  # int in range [0, 10]
            current = current.next

        print()
        k = random.randint(0, 10)
        print("in: " + '\t' + partition.print_linked_list(head) + " k-value: " + str(k))
        head = partition.partition(head, k)
        print("out: " + '\t' + partition.print_linked_list(head))



if __name__ == "__main__":
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestRemoveDups)
    # testResult = unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()