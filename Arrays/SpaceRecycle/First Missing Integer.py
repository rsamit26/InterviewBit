"""
Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space.
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        temp = []
        for i in A:
            if i > 0:
                temp.append(i)
        temp.sort()
        n = len(temp)
        o = temp[0]
        p = 1

        for i in range(n):
            o ^= temp[i]

        for i in range(n + 2):
            p ^= i
        return o ^ p


    def Method_2_firstMissingPositive(self, arr):
        count = 0
        for i in arr:
            if i > 0:
                count += 1

        if count == 0:
            return 1
        else:
            temp_arr = [0] * (max(arr) + 2)

            for i in range(0, len(arr)):
                if arr[i] > 0:
                    temp_arr[arr[i]] = 1
            for i in range(1, len(temp_arr)):
                if temp_arr[i] != 1:
                    return i


"""
Testing Code for this problem
"""

s = Solution()
arr = [3, 4, -1, 1]
print(s.Method_2_firstMissingPositive(arr))
print(s.firstMissingPositive(arr))
