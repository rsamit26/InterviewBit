"""
Given A, generate all structurally unique BST’s (binary search trees) that store values 1...A.

Example :
Given A = 3, your program should return all 5 unique BST’s shown below.


   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:

    def generate_unique_bst(self, n):
        return self.helper(1, n)

    def helper(self, low, high):

        result = []  # Creating a list to store all the nodes

        if low > high:
            result.append(None)
        for i in range(low, high + 1):
            left = self.helper(low, i - 1)
            right = self.helper(i + 1, high)

            for j in left:
                for k in right:
                    curr = Node(i)
                    curr.left = j
                    curr.right = k
                    result.append(curr)

        return result


from Python.Level6.TreeDataStructure import Node

s = Solution()
roots = s.generate_unique_bst(3)
for i in roots:
    print(i.tree_traversal(), end="")
