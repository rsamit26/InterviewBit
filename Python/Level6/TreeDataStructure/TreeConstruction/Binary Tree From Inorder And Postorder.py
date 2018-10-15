"""
Given inorder and postorder traversal of a tree, construct the binary tree.

 Note: You may assume that duplicates do not exist in the tree.
Example :

Input :
        Inorder : [2, 1, 3]
        Postorder : [2, 3, 1]

Return :
            1
           / \
          2   3
"""
# Inorder ::    left -> root -> right
# Postorder ::  left -> right -> root
# ::: From the post order traversal we can say last element is root of the tree
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
    def inPostConstruct(self, iarr, parr):
        lookup = {}
        for i, a in enumerate(iarr):
            lookup[a] = i
        return self.buildTreeRec(lookup, iarr, parr, len(parr), 0, len(iarr))

    def buildTreeRec(self, lookup, iarr, parr, post_end, in_str, in_end):

        #base case
        if in_str == in_end:
            return None
        root = Node(parr[post_end-1])

        idx = lookup[parr[post_end-1]]

        root.left = self.buildTreeRec(lookup, iarr, parr, post_end-1-(in_end-idx-1), in_str, idx)

        root.right = self.buildTreeRec(lookup, iarr, parr, post_end-1, idx+1, in_end)

        return root


s = Solution()
i = [2,1,3]
p = [2,3,1]
root = s.inPostConstruct(i,p)
root.treeTraversal()
