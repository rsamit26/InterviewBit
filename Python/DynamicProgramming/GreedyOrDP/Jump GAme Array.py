"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return 1 ( true ).

A = [3,2,1,0,4], return 0 ( false ).

Return 0/1 for this problem
"""

class Solution:

    def jumpArray(self, arr):
        n= len(arr)
        i, jump = 0,0
        while jump >= i and jump <= n-1:
            jump = max(jump, i+arr[i])
            i+= 1
        if jump >= n-1:
            return 1
        else: return 0
s = Solution()
ar = [3,2,1,0,0]
print(s.jumpArray(ar))
