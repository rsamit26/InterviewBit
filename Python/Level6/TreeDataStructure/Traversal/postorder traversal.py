"""Given a binary tree, return the postorder traversal of its nodes’ values.

Example :

Given binary tree

   1
    \
     2
    /
   3
return [3,2,1].

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
                stack.append((root, True))
                stack.append((root.right, False))
                stack.append((root.left, False))

        return result


""" Testing Code """
from Python.Level6.TreeDataStructure import Node

s = Solution()
root = Node(1)
root.right = Node(2)
root.right.left = Node(3)
print(s.inorder_traversal(root))