"""

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

A height balanced BST : a height-balanced binary tree is defined as a binary tree in which the depth of the two
subtrees of every node never differ by more than 1.
Example :


Given A : 1 -> 2 -> 3
A height balanced BST  :

      2
    /   \
   1     3
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:

    def list_to_BST(self, head):
        arr = []
        while head:
            arr.append(head.data)
            head = head.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

s = Solution()
print(s.list_to_BST(head))
