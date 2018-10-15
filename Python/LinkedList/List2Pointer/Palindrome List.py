"""
Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not,
respectively.

Notes:

Expected solution is linear in time and constant in space.
For example,

List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.
"""

from Python.Level4.LinkedList import Node, Traverse


class Solution:

    def is_palindrome(self, head):
        """
        Using list :
        append the value of linked list in a python array and checking if array and reverse of array is equal or not
        :param head:
        :return: isPalindrome
        """

        if not head or head.next is None:
            return True

        is_palindrome = 0

        values = []

        while head is not None:
            values.append(head.val)
            head = head.next

        if values == values[::-1]:
            is_palindrome = 1

        return is_palindrome

    def is_palindrome_02(self, head):
        """ Create a list by traversing the current list value
            Traverse both list :::
                if all values are equal then return 1
                else return 0
            """
        x = []
        p = head
        while p is not None:
            x.append(p.val)
            p = p.next
        i = len(x) - 1
        while head is not None and i > -1:
            if head.val != x[i]:
                return 0
            else:
                head = head.next
                i -= 1
        return 1

    def is_palindrome_03(self, head):
        reverse, fast = None, head
        # Reverse the first half part of the list.
        while fast and fast.next:
            fast = fast.next.next
            head.next, reverse, head = reverse, head, head.next

        # If the number of the nodes is odd,
        # set the head of the tail list to the next of the median node.
        tail = head.next if fast else head

        # Compare the reversed first half list with the second half list.
        # And restore the reversed first half list.
        is_palindrome = 1
        while reverse:
            is_palindrome = is_palindrome and reverse.val == tail.val
            reverse.next, head, reverse = head, reverse, reverse.next
            tail = tail.next

        return is_palindrome



if __name__ == "__main__":
    # initializing the linked list values
    # h1, h1.next, h1.next.next, h1.next.next.next, h1.next.next.next.next = Node(1), Node(4), Node(6), Node(4), Node(1)
    h2, h2.next, h2.next.next = Node(1), Node(2), Node(1)
    # printing the new list
    # Traverse().print_list(Solution().is_palindrome(h1))
    print(Solution().is_palindrome_02(h2))
    # print(Solution().is_palindrome(h2))
