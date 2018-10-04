"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be
set to NULL.

Initially, all next pointers are set to NULL.

 Note:
You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two
children).
Example :

Given the following perfect binary tree,

         1
       /  \
      2    5
     / \  / \
    3  4  6  7
After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 5 -> NULL
     / \  / \
    3->4->6->7 -> NULL
Note that using recursion has memory overhead and does not qualify for constant space.
"""


# Definition for a  binary tree node
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        head = root
        while head:
            prev, cur, next_head = None, head, None
            while cur:
                if next_head is None:
                    if cur.left:
                        next_head = cur.left
                    elif cur.right:
                        next_head = cur.right

                if cur.left:
                    if prev:
                        prev.next = cur.left
                    prev = cur.left

                if cur.right:
                    if prev:
                        prev.next = cur.right
                    prev = cur.right

                cur = cur.next
            head = next_head

