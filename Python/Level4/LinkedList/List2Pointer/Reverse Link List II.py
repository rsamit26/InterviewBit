"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->6->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.
"""

from Python.Level4.LinkedList import Node, Traverse


class Solution:

    def reverse_list(self, head, m, n):

        diff, dummy, cur = n - m + 1, Node(-1), head
        dummy.next = head

        last_unswapped = dummy
        while cur and m > 1:
            cur, last_unswapped, m = cur.next, cur, m - 1

        prev, first_swapped = last_unswapped, cur
        while cur and diff > 0:
            cur.next, prev, cur, diff = prev, cur, cur.next, diff - 1

        last_unswapped.next, first_swapped.next = prev, cur

        return dummy.next


if __name__ == "__main__":
    # initializing the linked list values
    h1, h1.next, h1.next.next, h1.next.next.next, h1.next.next.next.next, h1.next.next.next.next.next = Node(1), Node(
        2), Node(3), Node(4), Node(5), Node(6)
    # h1, h1.next, h1.next.next, h1.next.next.next, h1.next.next.next.next = Node(1), Node(2), Node(3), Node(4), Node(5)
    # h1, h1.next, h1.next.next = Node(1), Node(2), Node(3)
    # h2, h2.next, h2.next.next = Node(1), Node(2), Node(1)
    # printing the new list
    Traverse().print_list(Solution().reverse_list(h1, 2, 4))
