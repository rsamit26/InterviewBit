"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""


# class Solution:
#     def compare_2_numbers(self, a, b):
#         ab = str(a) + str(b)
#         ba = str(b) + str(a)
#         return cmp(int(ba), int(ab))
#
#     def largest_number(self, arr):
#         n = len(arr)
#
#         sorted(arr, cmp=self.compare_2_numbers)
#         return arr
#


"""
Testing Solution
"""

# s = Solution()
# print(s.largest_number([3, 30, 34, 5, 9]))