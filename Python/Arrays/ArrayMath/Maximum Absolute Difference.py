"""
You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.
"""


class Solution:
    # @param A : list of integers
    # @return an integer

    def max_arr(self, A):
        self.A = A
        max1 = -1000000000
        min1 = +1000000000
        max2 = -1000000000
        min2 = +1000000000
        for i in range(len(A)):
            max1 = max(max1, A[i] + i)
            min1 = min(min1, A[i] + i)
            max2 = max(max2, A[i] - i)
            min2 = min(min2, A[i] - i)

        return max(max1 - min1, max2 - min2)


"""Testing Code"""

s = Solution()
arr = [1, 3, -1]

print(s.max_arr(arr))
