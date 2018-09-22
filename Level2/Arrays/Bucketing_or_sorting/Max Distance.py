"""
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

If there is no solution possible, return -1.

Example :

A : [3 5 4 2]

Output : 2
for the pair (3, 4)
"""


class Solution:
    @staticmethod
    def max_distance(arr):
        n = len(arr)

        l_arr = [None] * n
        r_arr = [None] * n

        l_arr[0] = arr[0]
        for i in range(1, n):
            l_arr[i] = min(arr[i], l_arr[i - 1])

        r_arr[n - 1] = arr[n - 1]
        j = n - 2
        for j in range(n - 2, -1, -1):
            r_arr[j] = max(arr[j], r_arr[j + 1])

        i, j, diff = 0, 0, -1

        while j < n and i < n:

            if l_arr[i] <= r_arr[j]:
                diff = max(diff, j - i)
                j += 1
            else:
                i += 1
        return diff


s = Solution()
ar = [1, 2, 3]
print(s.max_distance(ar))
