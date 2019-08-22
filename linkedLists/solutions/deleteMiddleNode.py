"""
input: any node except the first or last from a linked list
output: None -- modify the given linked list without a middle node (any node that is not the first or the last)

Run instructions: --- currently no main method in deleteMiddleNode.py
python3 deleteMiddleNode.py node
"""

import sys

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

def deleteMiddleNode(node):
    if node is None or node.next is None:
        return
    node.value = node.next.value
    node.next = node.next.next

"""
if __name__ == "__main__":
    deleteMiddleNode(sys.argv[1])
"""