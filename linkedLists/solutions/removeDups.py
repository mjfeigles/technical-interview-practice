"""
input: an unsorted linked list
output: the same unsorted linked list without duplicates

Run instructions: --- currently no main method in removeDups.py
* see ../tests/test_removeDups.py to test file methods


Note: head is the head node
"""
import sys

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

def remove_dups(head):
    if head is None or head.next is None:
        return head
    map = {}
    current = head
    map[current.value] = 1
    while current != None and current.next != None:
        if current.next.value in map:
            current.next = current.next.next
            continue
        else:
            map[current.next.value] = 1
        current = current.next

    # print(map.keys())

    return head

def print_linked_list(head):
    if head is None:
        return "empty list"
    printed_list = ""
    while head is not None:
        printed_list = printed_list + str(head.value) + "->"
        head = head.next
    printed_list = printed_list[:len(printed_list)-2]
    return printed_list


