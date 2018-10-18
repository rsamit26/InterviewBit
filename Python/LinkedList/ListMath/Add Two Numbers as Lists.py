"""
You are given two linked lists representing two non-negative numbers. The digits
 are stored in reverse order and each of their nodes contain a single digit.
 Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

    342 + 465 = 807
Make sure there are no trailing zeros in the output list
So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def addTwoNumber_02(self, l1, l2):
        if l1 is None:  # if list1 is none return list2
            return l2
        elif l2 is None:  # if list2 is none return list1
            return l1
        else:
            l3 = curr = ListNode(0)  # create the new list head
            carry =0  # store carry of summation of two node value
            while l1 or l2 or carry:
                if l1:
                    carry += l1.val
                    l1 = l1.next
                if l2:
                    carry += l2.val
                    l2 = l2.next
                curr.next = ListNode(carry % 10)
                curr = curr.next
                carry //= 10
            return l3.next

    def addTwoNumber(self, l1, l2):
        temp,x,y = "", 0, 0
        while l1:
            temp += str(l1.val)
            l1 = l1.next
        x = int(temp[::-1])
        temp = ""
        while l2:
            temp += str(l2.val)
            l2 = l2.next
        y = int(temp[::-1])
        z = x+y
        temp = str(z)[::-1]
        l3 = ListNode(int(temp[0]))
        prev = l3
        for i in range(1,len(temp)):
            prev.next = ListNode(int(temp[i]))
            prev = prev.next

        return l3

    def printNode(self, head):

        while head:
            print(head.val, end="=>")
            head = head.next

s = Solution()
l1 = ListNode(2)
l1.next  = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next  = ListNode(6)
l2.next.next = ListNode(4)
# l3 = s.addTwoNumber(l1,l2)
# s.printNode(l3)

l4 = s.addTwoNumber_02(l1, l2)
s.printNode(l4)
