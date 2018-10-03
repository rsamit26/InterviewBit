"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along
the path equals the given sum.

Example :

Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""


from Python.Level6.TreeDataStructure import Node


class Solution:

    def path_sum(self, root, target):

        if root is None:
            return target == 0

        else:
            res = 0
            target -= root.data

            if target == 0 and root.left is None and root.right is None:
                return 1

            if root.left:
                res = res or self.path_sum(root.left, target)
            if root.right:
                res = res or self.path_sum(root.right, target)

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

print(s.path_sum(root, 22))
