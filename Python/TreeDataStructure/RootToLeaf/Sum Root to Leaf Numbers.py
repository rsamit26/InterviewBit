"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers % 1003.

Example :

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.

"""
from Python.Level6.TreeDataStructure import Node


class Solution:

    def sum_root_to_leaf(self, root):
        path = ""
        res = []
        self.helper(path, res, root)
        sum = 0
        for i in res:
            sum += int(i)
        return sum

    def helper(self, path, res, node):

        if not node:
            return res

        if node.left is None and node.right is None:
            res.append(path + str(node.data))
            return res

        path += str(node.data)
        self.helper(path, res, node.left)
        self.helper(path, res, node.right)
        return res


s = Solution()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(0)
print(s.sum_root_to_leaf(root))
