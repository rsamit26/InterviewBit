"""
Given a N cross M matrix in which each row is sorted, find the overall median of the matrix. Assume N*M is odd.

For example,

Matrix=
[1, 3, 5]
[2, 6, 9]
[3, 6, 9]

A = [1, 2, 3, 3, 5, 6, 6, 9, 9]

Median is 5. So, we return 5.
Note: No extra memory is allowed
"""

from bisect import bisect_right as upper_bound


class Solution:
    # @param A : list of list of integers
    # @return an integer
    MAX = 100

    def findMedian(self, A):
        R = len(A)
        C = len(A[0])
        mi = A[0][0]
        mx = 0
        for i in range(R):
            if A[i][0] < mi:
                mi = A[i][0]
            if A[i][C - 1] > mx:
                mx = A[i][C - 1]

        desired = (R * C + 1) / 2
        while mi < mx:
            mid = mi + (mx - mi) // 2
            place = [0]

            for i in range(R):
                j = upper_bound(A[i], mid)
                place[0] = place[0] + j
            if place[0] < desired:
                mi = mid + 1
            else:
                mx = mid
        return mi


"""
Testing Code
"""
s = Solution()
print(s.findMedian([[1, 3, 5],
                    [2, 6, 9],
                    [3, 6, 9]]))

# output :: 5
