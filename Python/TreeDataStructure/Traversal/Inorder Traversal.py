"""
Given a binary tree, return the inorder traversal of its nodes’ values.

Example :
Given binary tree

   1
    \
     2
    /
   3
return [1,3,2].

Using recursion is not allowed.
"""


class Solution:

    def inorder_traversal(self, root):

        result, stack = [], [(root, False)]

        while stack:
            root, is_flaged = stack.pop()
            if root is None:
                continue
            if is_flaged:
                result.append(root.data)
            else:
                stack.append((root.right, False))
                stack.append((root, True))
                stack.append((root.left, False))

        return result

    # Method 02 : Using recursion
    def inorderTraversal(self, root):
        res = []
        if root is None:
            return []
        self.helper(root, res)
        return res
    def helper(self, root, res):
        if root is None:
            return
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)


""" Testing Code """
from Python.Level6.TreeDataStructure import Node

s = Solution()
root = Node(1)
root.right = Node(2)
root.right.left = Node(3)
print(s.inorder_traversal(root))
