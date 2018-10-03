"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 Note:
You may only use constant extra space.
Example :

Given the following binary tree,

         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
"""


class TreeLinkNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.data, repr(self.next))

class Solution:

    def populate_next_r_02(self, root):

        if root is None:
            return

        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                head = root
                while head.next:
                    if head.next.left:
                        root.left.next = head.next.left
                        break
                    elif head.next.right:
                        root.left.next = head.next.right
                        break
                    head = head.next

        if root.right:
            head = root

            while head.next:
                if head.next.left:
                    root.right.next = head.next.left
                    break
                elif head.next.right:
                    root.right.next = head.next.right

                head = head.next

        self.populate_next_r_02(root.right)
        self.populate_next_r_02(root.left)


    def populate_next_r(self, root):
        while root:
            curr = root
            while curr and curr.left:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            root = root.left







if __name__ == "__main__":
    root, root.left, root.right = TreeLinkNode(1), TreeLinkNode(2), TreeLinkNode(3)
    root.left.left, root.left.right,root.right.left, root.right.right = TreeLinkNode(4), TreeLinkNode(5),TreeLinkNode(6), TreeLinkNode(7)
    Solution().populate_next_r(root)
    print(root)
    print(root.left)
    print(root.left.left)
    Solution().populate_next_r_02(root)
    print()
    print(root)
    print(root.left)
    print(root.left.left)



