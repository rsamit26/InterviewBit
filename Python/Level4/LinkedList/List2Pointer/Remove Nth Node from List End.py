"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

 Note:
If n is greater than the size of the list, remove the first node of the list.
Try doing it using constant additional space.
"""
from Python.Level4.LinkedList import Node, Traverse


class Solution:

    def remove_nth_node(self, head, k):
        count = 0
        prev = head
        curr_ptr = head
        temp = head
        length = 0
        while temp is not None:
            length += 1
            temp = temp.next
        if head is not None:
            while count < k:
                if prev is None:
                    head = curr_ptr.next
                    head.next = curr_ptr.next.next
                    return head
                prev = prev.next
                count += 1
        if count == length:
            head = curr_ptr.next
            return head
        elif count == 0:
            while curr_ptr.next is not None:
                prev = curr_ptr
                curr_ptr = curr_ptr.next
            prev.next = None
            return head
        else:
            while prev.next is not None:
                curr_ptr = curr_ptr.next
                prev = prev.next
            curr_ptr.next = curr_ptr.next.next
            return head


if __name__ == "__main__":
    # initializing the linked list values
    h1, h1.next, h1.next.next, h1.next.next.next = Node(1), Node(2), Node(3), Node(4)
    # h2, h2.next, h2.next.next, h2.next.next.next = Node(4), Node(5), Node(6), Node(7)
    # printing the new list
    Traverse().print_list(Solution().remove_nth_node(h1, 6))
