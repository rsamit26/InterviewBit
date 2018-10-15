"""
Given a binary tree, return the zigzag level order traversal of its nodes’ values. (ie, from left to right,
then right to left for the next level and alternate between).

Example :
Given binary tree

              3
            /   \
           /     \
          9      20
         / \    /  \
        4   6  15   7
return

[
         [3],
         [20, 9],
         [4, 6,15, 7]
]
"""


class Solution:

    def zigzag_traversal(self, root):

        if root is None:
            return []

        else:
            queue = []
            h_node = {}
            v_dis = {root: 0}
            queue.append(root)
            h_node[0] = [root.data]

            while queue:
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                    v_dis[curr.left] = v_dis[curr] + 1
                    vd = v_dis[curr.left]
                    if h_node.get(vd) is None:
                        h_node[vd] = []
                    h_node[vd].append(curr.left.data)

                if curr.right:
                    queue.append(curr.right)
                    v_dis[curr.right] = v_dis[curr] + 1
                    vd = v_dis[curr.right]
                    if h_node.get(vd) is None:
                        h_node[vd] = []
                    h_node[vd].append(curr.right.data)
        result = []
        for k in h_node.keys():
            if k % 2 == 0:
                result.append(h_node[k])
            else:
                h_node[k].reverse()
                result.append(h_node[k])
        return result


class Solution02:

    def zigzag_traversal(self, root):
        result, queue = [], [(root, 0)]

        while queue:
            root, depth = queue.pop(0)

            if root:
                if len(result) < depth + 1:
                    result.append([])
                if depth % 2:
                    result[depth].insert(0, root.data)
                else:
                    result[depth].append(root.data)

                queue.append((root.left, depth + 1))
                queue.append((root.right, depth + 1))
        return result


from Python.Level6.TreeDataStructure import Node

s = Solution()
root = Node(3)

root.left = Node(9)
root.right = Node(20)
root.left.left = Node(4)
root.left.right = Node(6)
root.right.left = Node(15)
root.right.right = Node(7)
# root.right.left.right = Node(8)
# root.right.right.left = Node(10)
# root.right.right.right = Node(9)
# root.right.right.left.right = Node(11)
# root.right.right.left.right.right = Node(12)
print(s.zigzag_traversal(root))

s2 = Solution02()
print(s2.zigzag_traversal(root))
