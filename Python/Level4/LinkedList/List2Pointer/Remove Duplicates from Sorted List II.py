"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers
from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""

from Python.Level4.LinkedList import Node, Traverse


class Solution:
    def remove_duplicates(self, head):

        temp = Node(0)

        prev, curr = temp, head

        while curr:
            if curr.next and curr.next.val == curr.val:
                val = curr.val
                while curr and curr.val == val:
                    curr = curr.next
                prev.next = curr
            else:
                prev.next = curr
                prev = curr
                curr = curr.next
        return temp.next




"""Testing Code """

if __name__ == "__main__":
    # initializing the linked list values
    head, head.next, head.next.next = Node(1), Node(1), Node(3)
    head.next.next.next, head.next.next.next.next = Node(4), Node(4)
    head.next.next.next.next.next, head.next.next.next.next.next.next = Node(4), Node(4)
    # printing the new list
    Traverse().print_list(Solution().remove_duplicates(head))
