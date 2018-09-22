"""
Given an array of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum
XOR value.

Examples :
Input
0 2 5 7
Output
2 (0 XOR 2)
Input
0 4 7 9
Output
3 (4 XOR 7)

Constraints:
2 <= N <= 100 000
0 <= A[i] <= 1 000 000 000

"""
import sys


class Solution:
    def min_xor(self, arr):
        n = len(arr)
        arr.sort()

        min_xor = arr[0] ^ arr[1]

        for i in range(1, n - 1):
            val = arr[i] ^ arr[i + 1]
            min_xor = min(min_xor, val)

        return min_xor


s = Solution()
ar = [2, 0]
print(s.min_xor(ar))
