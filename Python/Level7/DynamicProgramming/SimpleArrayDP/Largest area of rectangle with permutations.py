"""
Given a binary grid i.e. a 2D grid only consisting of 0’s and 1’s, find the area of the largest rectangle inside the
grid such that all the cells inside the chosen rectangle should have 1 in them. You are allowed to permutate the columns
matrix i.e. you can arrange each of the column in any order in the final grid. Please follow the below example for
more clarity.

Lets say we are given a binary grid of 3 * 3 size.

1 0 1

0 1 0

1 0 0

At present we can see that max rectangle satisfying the criteria mentioned in the problem is of 1 * 1 = 1 area i.e
either of the 4 cells which contain 1 in it. Now since we are allowed to permutate the columns of the given matrix,
we can take column 1 and column 3 and make them neighbours. One of the possible configuration of the grid can be:

1 1 0

0 0 1

1 0 0

Now In this grid, first column is column 1, second column is column 3 and third column is column 2 from the original
given grid. Now, we can see that if we calculate the max area rectangle, we get max area as 1 * 2 = 2 which is bigger
than the earlier case. Hence 2 will be the answer in this case.
"""


class Solution:

    def largest_area_rec(self, arr):

        m = len(arr)
        n = len(arr[0])

        temp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(n):
            temp[0][i] = arr[0][i]
            for j in range(1, m):
                if arr[j][i] == 0:
                    temp[j][i] = 0
                else:
                    temp[j][i] = temp[j - 1][i] + 1

        for i in range(len(temp)):
            temp[i].sort(reverse=True)
        max_area = 0

        for i in range(m):
            for j in range(n):
                curr = (j + 1) * temp[i][j]

                if curr > max_area:
                    max_area = curr
        return max_area


""" Testing Code"""
s = Solution()
ar = [[1, 0, 1], [0, 1, 0], [1, 0, 0]]
print(s.largest_area_rec(ar))
