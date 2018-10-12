"""
Given a binary tree, return the level order traversal of its nodes’ values. (ie, from left to right, level by level).

Example :
Given binary tree

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
Also think about a version of the question where you are asked to do a level order traversal of the tree when depth
of the tree is much greater than number of nodes on a level.
"""


class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:

    def level_order(self, root):

        if root is None:
            return []

        result = []
        queue = [root]

        while queue:
            level = len(queue)
            temp_node = []
            for _ in range(level):
                node = queue.pop(0)
                temp_node.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(temp_node)
        return result


s = Solution()
root = Tree(3)
root.left = Tree(9)
root.right = Tree(20)
root.right.left = Tree(15)
root.right.right = Tree(7)

print(s.level_order(root))
