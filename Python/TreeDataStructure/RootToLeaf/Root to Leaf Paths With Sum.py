"""
Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.

For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return

[
   [5,4,11,2],
   [5,8,4,5]
]
"""

from Python.Level6.TreeDataStructure import Node


class Solution:

    def path_r_l_sum(self, root, target):

        path, res = [], []
        self.path_r_l_sum_helper(root, res, path, target)
        return res

    def path_r_l_sum_helper(self, root, res, path, target):
        if not root:
            return res

        if root.left is None and root.right is None and root.data == target:
            res.append(path + [root.data])
            return res

        path.append(root.data)
        self.path_r_l_sum_helper(root.left, res, path, target - root.data)
        self.path_r_l_sum_helper(root.right, res, path, target - root.data)
        path.pop()
        return res


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
print(s.path_r_l_sum(root, 22))
