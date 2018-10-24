"""
Given two binary trees, write a function to check if they are equal or notself.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Example :

Input :

   1       1
  / \     / \
 2   3   2   3

Output :
  1 or True
"""
class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def isSameTree(self, p, q):
        if p is None and q is None:
            return 1
        if p is None or q is None:
            return 0
        return int((p.val == q.val)) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right , q.right)

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
print(s.isSameTree(root, root2))
