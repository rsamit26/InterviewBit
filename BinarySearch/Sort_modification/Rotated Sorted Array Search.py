"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).

You are given a target value to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Input : [4 5 6 7 0 1 2] and target = 4
Output : 0
"""


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search1(self, A, l, h, B):
        if l > h:
            return -1
        mid = (l + h) // 2
        if A[mid] == B:
            return mid
        if A[l] <= A[mid]:
            if A[l] <= B <= A[mid]:
                return self.search1(A, l, mid - 1, B)
            return self.search1(A, mid + 1, h, B)

        if A[mid] <= B <= A[h]:
            return self.search1(A, mid + 1, h, B)
        return self.search1(A, l, mid - 1, B)

    def search(self, A, B):
        l = 0
        h = len(A) - 1
        return self.search1(A, l, h, B)


""" 
Testing Code 
"""

s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 4))

# Output :: 0
