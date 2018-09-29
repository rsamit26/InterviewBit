"""
Given a singly linked list, modify the value of first half nodes such that :

1st node’s new value = the last node’s value - first node’s current value
2nd node’s new value = the second last node’s value - 2nd node’s current value,
and so on …

 NOTE :
If the length L of linked list is odd, then the first half implies at first floor(L/2) nodes. So, if L = 5, the first
half refers to first 2 nodes.
If the length L of linked list is even, then the first half implies at first L/2 nodes. So, if L = 4, the first half
refers to first 2 nodes.
Example :

Given linked list 1 -> 2 -> 3 -> 4 -> 5,

You should return 4 -> 2 -> 3 -> 4 -> 5
as

for first node, 5 - 1 = 4
for second node, 4 - 2 = 2
Try to solve the problem using constant extra space.
"""

from Python.Level4.LinkedList import Node, Traverse


class Solution:

    def substract(self, head):
        curr, count, i = head, 0, 0

        temp = head
        temp_arr = []

        while temp is not None:
            temp_arr.append(temp.val)
            temp = temp.next

            count += 1
        while i < count // 2:
            curr.val = temp_arr.pop() - curr.val
            curr = curr.next
            i += 1

        return head


if __name__ == "__main__":
    # initializing the linked list values
    # h1, h1.next, h1.next.next, h1.next.next.next, h1.next.next.next.next, h1.next.next.next.next.next = Node(1), Node(
    #     2), Node(3), Node(4), Node(5), Node(6)
    h1, h1.next, h1.next.next = Node(1), Node(3), Node(4)

    Traverse().print_list(Solution().substract(h1))
