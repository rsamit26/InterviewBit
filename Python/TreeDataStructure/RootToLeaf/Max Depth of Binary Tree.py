"""
Given a binary tree, find its maximum depth.

The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest
leaf node.

NOTE : The path has to end on a leaf node.
"""
from Python.Level6.TreeDataStructure import Node


class Solution:

    def max_depth(self, root):

        if root is None:
            return 0
        else:

            ld = self.max_depth(root.left)
            rd = self.max_depth(root.right)

            if ld > rd:
                return ld + 1
            else:
                return rd + 1


"""Testing program"""
s = Solution()
root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.right.left = Node(13)
root.right.right = Node(4)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.right.right = Node(1)
root.right.right.left = Node(5)
root.right.right.left.right = Node(90)

print(s.max_depth(root))
