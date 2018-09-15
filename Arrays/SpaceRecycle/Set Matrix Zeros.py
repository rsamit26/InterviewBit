"""
Given an m x n matrix of 0s and 1s, if an element is 0, set its entire row and column to 0.

Do it in place.
"""


class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, matrix):
        rows = set()
        columns = set()

        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 0:
                    rows.add(y)
                    columns.add(x)

        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if y in rows or x in columns:
                    matrix[y][x] = 0
        return matrix


"""
Testing Code
"""

matrix = [[1, 0, 1], [1, 1, 1], [1, 1, 1]]

s = Solution()
print(s.setZeroes(matrix))