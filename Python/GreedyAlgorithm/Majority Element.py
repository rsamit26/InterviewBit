"""
Given an array of size n, find the majority element. The majority element is the element that appears more than
floor(n/2) times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example :

Input : [2, 1, 2]
Return  : 2 which occurs 2 times which is greater than 3/2.
"""


class Solution:

    def majority_element(self, arr):
        n = len(arr)
        f = n//2
        from collections import Counter
        d = Counter(arr)
        p = d.most_common(1)
        if p[0][1] > f:
            return p[0][0]
        else:
            return 0

    def method_02(self, arr):

        n = len(arr)

        for i in arr:
            if arr.count(i) > n//2:
                return i


s = Solution()
a = [1, 1, 1, 2, 2]
print(s.majority_element(a))
print(s.method_02(a))
