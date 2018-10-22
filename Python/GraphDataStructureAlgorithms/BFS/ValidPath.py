"""
There is a rectangle with left bottom as  (0, 0) and right up as (x, y). There
are N circles such that their centers are inside the rectangle.
Radius of each circle is R. Now we need to find out if it is possible that we
can move from (0, 0) to (x, y) without touching any circle.

Note : We can move from any cell to any of its 8 adjecent neighbours and we
cannot move outside the boundary of the rectangle at any point of time.

1st argument given is an Integer x.
2nd argument given is an Integer y.
3rd argument given is an Integer N, number of circles.
4th argument given is an Integer R, radius of each circle.
5th argument given is an Array A of size N, where A[i] = x cordinate of ith circle
6th argument given is an Array B of size N, where B[i] = y cordinate of ith circle
Output Format

Return YES or NO depending on weather it is possible to reach cell (x,y) or not
starting from (0,0).

0 <= x, y, R <= 100
1 <= N <= 1000
Center of each circle would lie within the grid
"""

class Solution:
    import sys
    sys.setrecursionlimit(100000000)
    moves = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
    def valid_path(self, x, y, n, r, xarr, yarr):

        visited = [[False for _ in range(x+1)] for _ in range(y+1)]

        if self.dfs(0, 0, visited, x, y, n, r, xarr, yarr):
            return 'YES'
        else:
            return 'NO'
    def dfs(self, y0,x0, visited, x, y, n, r, xarr, yarr):

        if x0 == x and y0 == y:
            return True

        visited[x0][y0] = True

        for move in Solution.moves:
            tx,ty = move
            if 0 <= y0+ty <= y and 0 <= x0+tx <= x and not visited[y0+ty][x0+tx]:
                if not self.circle(r, xarr,yarr, y0 + ty, x0+tx) and self.dfs(y0+ty, x0 + tx, visited, x, y, n, r, xarr, yarr):
                    return True
        return False

    def circle(self, r, xarr, yarr, y,x):
        for j in range(len(xarr)):
            if ((xarr[j]-x)**2 + (yarr[j] -y)**2)**0.5 <= r:
                return True
        else:
            return False
