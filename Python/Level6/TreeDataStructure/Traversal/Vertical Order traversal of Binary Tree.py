"""
Given a binary tree, print a vertical order traversal of it.

Example :
Given binary tree:

      6
    /   \
   3     7
  / \     \
 2   5     9
returns

[
    [2],
    [3],
    [6 5],
    [7],
    [9]
]


Note : If 2 Tree Nodes shares the same vertical level then the one with lesser depth will come first.

"""

from Python.Level6.TreeDataStructure import Node


class Solution:

    def vertical_traversal(self, root):

        from collections import OrderedDict

        if root is None:  # If root not found return empty list
            return []

        queue = []  # Empty queue for level wise traversal

        v_node = {}  # dict for mapping node data at same horizontal distance from root node

        hd_node = {}  # horizontal distance of node

        queue.append(root)  # append root in the queue
        hd_node[root] = 0  # set horizontal distance of root is 0
        v_node[0] = [root.data]  # store root data at 0 distance

        while len(queue) > 0:  # iterate over the queue till queue become empty

            curr = queue.pop(0)  # start with root element

            if curr.left:  # If node has left then append it in the queue
                queue.append(curr.left)
                # set horizontal distance for curr node to hd_distance -1 since it is in left of root element
                hd_node[curr.left] = hd_node[curr] - 1

                hd = hd_node[curr.left]  # horizontal distance of curr.left from root

                if v_node.get(hd) is None:  # if none of the node is at hd the append the node data at hd in v_node
                    v_node[hd] = []
                v_node[hd].append(curr.left.data)

            if curr.right:

                queue.append(curr.right)

                hd_node[curr.right] = hd_node[curr] + 1
                hd = hd_node[curr.right]

                if v_node.get(hd) is None:
                    v_node[hd] = []
                v_node[hd].append(curr.right.data)
        sorted_m = OrderedDict(sorted(v_node.items()))  # sort the dict in order using distance
        return list(sorted_m.values())


s = Solution()
root = Node(1)

root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.left = Node(10)
root.right.right.right = Node(9)
root.right.right.left.right = Node(11)
root.right.right.left.right.right = Node(12)
print(s.vertical_traversal(root))
root.tree_traversal()
