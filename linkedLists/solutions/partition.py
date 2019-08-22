"""
input: head node and value k
output: same linked list with all nodes in linked list <= k at the front of the list and all nodes in linked list > k
at the end of the linked list (order not specific)

Run instructions -- no main method in partition.py
* see test_partition.py
"""

import sys

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

def print_linked_list(head):
    if head is None:
        return "empty list"
    printed_list = ""
    while head is not None:
        printed_list = printed_list + str(head.value) + "->"
        head = head.next
    printed_list = printed_list[:len(printed_list) - 2]
    return printed_list

def partition(node, k):
    if node is None:
        return None

    head, tail = node, node

    while node is not None:
        nextNode = node.next
        if node.value >= k:
            tail.next = node
            tail = tail.next
        else:
            node.next = head
            head = node
        node = nextNode

    tail.next = None

    return head
