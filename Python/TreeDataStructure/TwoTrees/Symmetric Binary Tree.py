"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

Example :

    1
   / \
  2   2
 / \ / \
3  4 4  3
The above binary tree is symmetric.
But the following is not:

    1
   / \
  2   2
   \   \
   3    3
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""
class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def isSymmetric(self, root):
        if root is None:
            return True
        return int(self.helper(root.left, root.right))

    def helper(self, node1, node2):

        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        return node1.val == node2.val and self.helper(node1.left, node2.right) and self.helper(node1.right, node2.left)
s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
print(s.isSameTree(root))
