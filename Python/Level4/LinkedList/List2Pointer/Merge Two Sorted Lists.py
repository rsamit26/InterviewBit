"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.

For example, given following linked lists :

  5 -> 8 -> 20
  4 -> 11 -> 15
The merged list should be :

4 -> 5 -> 8 -> 11 -> 15 -> 20
"""

from Python.Level4.LinkedList import Node, Traverse


class Solution:

    def merge(self, h1, h2):

        p1 = h1
        p2 = h2
        new_head = None

        while (p1 is not None) and (p2 is not None):

            if p1.val < p2.val:
                e = Node(p1.val)
                e.next = new_head
                new_head = e
                p1 = p1.next
            else:
                e = Node(p2.val)
                e.next = new_head
                new_head = e
                p2 = p2.next

        while p1 is not None:
            e = Node(p1.val)
            e.next = new_head
            new_head, p1 = e, p1.next

        while p2 is not None:
            e = Node(p2.val)
            e.next = new_head
            new_head, p2 = e, p2.next

        # Reversing the list
        prev = None
        current = new_head
        while current is not None:
            nx = current.next
            current.next = prev
            prev = current
            current = nx
            new_head = prev

        return new_head


"""Testing Code """

if __name__ == "__main__":
    # initializing the linked list values
    h1, h1.next, h1.next.next = Node(1), Node(2), Node(3)
    h2, h2.next, h2.next.next, h2.next.next.next = Node(4), Node(5), Node(6), Node(7)
    # printing the new list
    Traverse().print_list(Solution().merge(h1, h2))
