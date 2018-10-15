"""
Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example :

Input :
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]

Output : [3 3 5]

Input :
    A : [1 2 3 3 4 5 6]
    B : [3 5]

Output : [3 5]
"""


class Solution:
    # @param a : tuple of integers
    # @param b : tuple of integers
    # @return a list of integers
    def intersection_array(self, a, b):
        res = []
        m = len(a)
        n = len(b)
        i, j = 0, 0

        while i < m and j < n:
            # if a[i] = b[j] the increase the pointer in both array
            if a[i] == b[j]:
                res.append(a[i])
                i += 1
                j += 1
            # Since array is sorted if a[i] < b[j], increase pointer of a by 1
            elif a[i] < b[j]:
                i += 1
            # Since array is sorted if a[i] > b[j], increase pointer of b by 1
            elif a[i] > b[j]:
                j += 1
        return res


"""
Testing Solution
"""
s = Solution()
a = [1, 2, 3, 3, 4, 5, 6]
b = [0]
print(s.intersection_array(a, b))
