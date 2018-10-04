"""
Given an array of integers, find the length of longest subsequence which is first increasing then decreasing.

**Example: **

For the given array [1 11 2 10 4 5 2 1]

Longest subsequence is [1 2 10 4 2 1]

Return value 6
"""


class Solution:

    def longestSubsequenceLength(self, A):
        n = len(A)
        lis = [1] * n
        nas = [1] * n
        for i in range(n):
            for j in range(i):
                if A[i] > A[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1

        for i in range(n - 2, -1, -1):
            for j in range(n - 1, i, -1):
                if A[i] > A[j] and nas[i] < nas[j] + 1:
                    nas[i] = nas[j] + 1

        maximum = 0

        # Pick maximum of all LIS values
        for i in range(n):
            maximum = max(maximum, lis[i] + nas[i] - 1)

        return maximum


s = Solution()

ar = [1, 11, 2, 10, 4, 5, 2, 1]
print(s.longestSubsequenceLength(ar))