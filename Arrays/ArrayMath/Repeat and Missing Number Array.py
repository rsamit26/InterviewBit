"""
You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3]

Output:[3, 4]

A = 3, B = 4
"""


class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        A = list(A)
        p = 0
        m = 0
        for i in range(len(A)):
            if (A[abs(A[i]) - 1]) > 0:
                A[abs(A[i]) - 1] = -A[abs(A[i]) - 1]
            else:
                p = abs(A[i])

        for i in range(len(A)):
            if A[i] > 0:
                m = i + 1

        return [p, m]


"""
Testing code
"""

arr = [3, 1, 2, 5, 3]

s = Solution()

print(s.repeatedNumber(arr))

# repeating = 3 , missing = 4
