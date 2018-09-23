"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

"""
from Python.Level4.LinkedList import Node, Traverse


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def delete_duplicates(self, head):
        if not head:
            return head
        ptr1 = head
        ptr2 = head.next

        while ptr2:
            if ptr1.val == ptr2.val:
                # Remove the node
                ptr1.next = ptr2.next
            else:
                ptr1 = ptr1.next
            ptr2 = ptr2.next
        return head


"""Testing Code """

if __name__ == "__main__":
    # initializing the linked list values
    head, head.next, head.next.next = Node(1), Node(1), Node(2)
    head.next.next.next, head.next.next.next.next = Node(3), Node(3)
    # printing the new list
    Traverse().print_list(Solution().delete_duplicates(head))
