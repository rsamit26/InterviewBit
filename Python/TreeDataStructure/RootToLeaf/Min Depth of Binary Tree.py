"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

 NOTE : The path has to end on a leaf node.
Example :

         1
        /
       2
min depth = 2.


"""

from Python.Level6.TreeDataStructure import Node


class Solution:

    def min_depth(self, root):

        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        if root.left is None:
            return self.min_depth(root.right) + 1
        if root.right is None:
            return self.min_depth(root.left) + 1

        return min(self.min_depth(root.left), self.min_depth(root.right)) + 1

    def min_depth_02(self, root):

        if root is None:
            return 0

        queue = []
        queue.append((root, 1))

        while queue:
            node, depth = queue.pop()

            if node.left is None and node.right is None:
                return depth

            if node.left is not None:
                queue.append((node.left, depth + 1))

            if node.right is not None:
                queue.append((node.right, depth + 1))


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

print(s.min_depth(root))
print(s.min_depth_02(root))
