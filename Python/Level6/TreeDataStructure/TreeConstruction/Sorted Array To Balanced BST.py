"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

Balanced tree : a height-balanced binary tree is defined as a binary tree in which the depth of
the two subtrees of every node never differ by more than 1.
Example :


Given A : [1, 2, 3]
A height balanced BST  :

      2
    /   \
   1     3
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def constuctBst(self, arr):
        n = len(arr)
        if n == 0:
            return
        mid = n//2
        root = Node(arr[mid])
        root.left = self.constuctBst(arr[:mid])
        root.right = self.constuctBst(arr[mid+1:])

        return root


s = Solution()
ar = [-1,-2,-3,-4,-5,0,1,2,3,4,5,6,7,8,9,10]
root = s.constuctBst(ar)
