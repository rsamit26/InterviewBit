"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note that if you end up using an additional array, you will only receive partial score.

Example:

If the array is

[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:

[
    [3, 1],
    [4, 2]
]
"""


class Solution:
    def rotate_array(self, arr):

        n = len(arr)

        for i in range(n // 2):
            for j in range(i, n - i - 1):
                temp = arr[i][j]
                arr[i][j] = arr[n - 1 - j][i]
                arr[n - 1 - j][i] = arr[n - 1 - i][n - 1 - j]
                arr[n - 1 - i][n - 1 - j] = arr[j][n - 1 - i]
                arr[j][n - 1 - i] = temp

        return arr


s = Solution()
ar = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
s.rotate_array(ar)
