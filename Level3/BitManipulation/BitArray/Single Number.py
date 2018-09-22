"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example :

Input : [1 2 2 3 1]
Output : 3
"""


class Solution:
    def find_one(self, arr):
        n = len(arr)
        p = arr[0]
        for i in range(1, n):
            p ^= arr[i]
        return p


s = Solution()
a = [1, 2, 3, 1, 3]
print(s.find_one(a))
