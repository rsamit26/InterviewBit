"""
Given preorder and inorder traversal of a tree, construct the binary tree.

 Note: You may assume that duplicates do not exist in the tree.
Example :

Input :
        Preorder : [1, 2, 3]
        Inorder  : [2, 1, 3]

Return :
            1
           / \
          2   3
"""
# Inorder ::    left -> root -> right
# Preorder ::   root -> left -> right
# ::: From the pre order traversal we can say first element is root of the tree
# save the value and index of inorder list in hashTable(dict) for fast lookup in O(1) time
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def treeTraversal(self):
        if self.left:
            self.left.treeTraversal()
        print(self.data)
        if self.right:
            self.right.treeTraversal()

class Solution:

    def inPreConstruct(self, inarr, prearr):
        lookup = {}
        for i, item in enumerate(inarr):
            lookup[item] = i
        return self.helper(lookup, inarr, prearr, 0, 0, len(inarr))

    def helper(self,lookup, inarr, prearr, pre_str, in_str, in_end):

        if in_str == in_end:
            return None
        root = Node(prearr[pre_str])

        idx = lookup[prearr[pre_str]]

        root.left = self.helper(lookup, inarr, prearr, pre_str+1, in_str , idx)
        root.right = self.helper(lookup, inarr, prearr, pre_str+1+idx-in_str, idx+1, in_end)
        return root


    def method_02(self, prearr, inarr):

        if not inarr:
            return None
        ridx = inarr.index(prearr[0])
        root = Node(prearr[0])

        root.left = self.method_02(prearr[1: ridx+1], inarr[:ridx])
        root.right = self.method_02(prearr[ridx+1: ], inarr[ridx+1:])
        return root

s = Solution()
i = [2,1,3]
p = [1,2,3]
root = s.inPreConstruct(i,p)
root.treeTraversal()
nroot = s.method_02(p,i)
nroot.treeTraversal()
