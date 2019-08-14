"""
input: an unsorted linked list
output: the same unsorted linked list without duplicates

Run instructions:
python3 remove_dups.py head
Note: head is the head node
"""
import sys

class Node:

    def __init__(self, value):
        self.next = None
        self.value = value

def remove_dups(head: Node):
    if head is None or head.next is None:
        return head

    map = {}

    current = head

    while current.next != None:
        if current.next.value in map:
            current.next = current.next.next
        else:
            map[current.next.value] = 1
        current = current.next

    return head


if __name__ == "__main__":
    remove_dups(sys.argv[1])