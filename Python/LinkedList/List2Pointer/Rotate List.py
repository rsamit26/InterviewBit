"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:

Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""
from Python.Level4.LinkedList import Node, Traverse


class Solution:

    def rotate_list(self, head, k):

        if not head or not head.next:
            return head
        count = 1
        curr = head
        while curr.next is not None:
            count += 1
            curr = curr.next
        curr.next = head

        curr, last, i = head, curr, 0

        while i < (count - k % count):
            last = curr
            curr = curr.next
            i += 1
        last.next = None
        return curr


if __name__ == "__main__":
    # initializing the linked list values
    h1, h1.next, h1.next.next, h1.next.next.next, h1.next.next.next.next, h1.next.next.next.next.next = Node(1), Node(
        2), Node(3), Node(4), Node(5), Node(6)
    # h1, h1.next, h1.next.next, h1.next.next.next, h1.next.next.next.next = Node(1), Node(2), Node(3), Node(4), Node(5)
    # h1, h1.next, h1.next.next = Node(1), Node(2), Node(3)
    # h2, h2.next, h2.next.next = Node(1), Node(2), Node(1)
    # printing the new list
    Traverse().print_list(Solution().rotate_list(h1, 89))
    # print(Solution().is_palindrome_02(h2))
    # print(Solution().is_palindrome(h2))
