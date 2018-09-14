"""
Python 3
"""


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def cover_points(self, A, B):
        mn = 0
        for i in range(1, len(A)):
            mn += max(abs(A[i] - A[i - 1]), abs(B[i] - B[i - 1]))

        return mn


"""
Testing Code for this problem
"""

s = Solution()
A = [0, 1, 1]
B = [0, 1, 2]

print(s.cover_points(A, B))

# output == 2
