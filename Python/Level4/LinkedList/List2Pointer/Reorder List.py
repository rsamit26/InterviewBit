"""
Given a singly linked list

    L: L0 → L1 → … → Ln-1 → Ln,
reorder it to:

    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
You must do this in-place without altering the nodes’ values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

"""
from Python.Level4.LinkedList import Node, Traverse


class Solution:

    def reorder_list(self, head):

        ptr1 = head
        count = 0
        temp = head
        while temp is not None:
            count += 1
            temp = temp.next
        i = 0
        new_head = head
        pre = head
        while i < (count // 2):
            pre = new_head
            new_head = new_head.next
            i += 1
        pre.next = None
        ptr3 = None
        while ptr1 is not None:
            ptr2 = new_head
            while ptr2.next is not None:
                ptr3 = ptr2
                ptr2 = ptr2.next
            ptr4 = ptr1.next
            ptr1.next = ptr2
            ptr2.next = ptr4
            if ptr3 is not None:
                ptr3.next = None
            ptr1 = ptr4
        res = head
        if count % 2 != 0:
            while res.next is not None:
                res = res.next
            res.next = ptr3
        return head


if __name__ == "__main__":
    # initializing the linked list values
    # h1, h1.next, h1.next.next, h1.next.next.next, h1.next.next.next.next, h1.next.next.next.next.next = Node(1), Node(
    #     2), Node(3), Node(4), Node(5), Node(6)
    # h1, h1.next, h1.next.next, h1.next.next.next, h1.next.next.next.next = Node(1), Node(2), Node(3), Node(4), Node(5)
    h1, h1.next,h1.next.next = Node(1), Node(2), Node(3)
    # h2, h2.next, h2.next.next = Node(1), Node(2), Node(1)
    # printing the new list
    Traverse().print_list(Solution().reorder_list(h1))
    # print(Solution().is_palindrome_02(h2))
    # print(Solution().is_palindrome(h2))
