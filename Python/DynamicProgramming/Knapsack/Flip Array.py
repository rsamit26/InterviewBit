"""
Given an array of positive elements, you have to flip the sign of some of its
elements such that the resultant sum of the elements of array should be minimum
non-negative(as close to zero as possible). Return the minimum no. of elements
whose sign needs to be flipped such that the resultant sum is minimum non-negative.

Constraints:

 1 <= n <= 100
Sum of all the elements will not exceed 10,000.

Example:

A = [15, 10, 6]
ans = 1 (Here, we will flip the sign of 15 and the resultant sum will be 1 )

A = [14, 10, 4]
ans = 1 (Here, we will flip the sign of 14 and the resultant sum will be 0)
"""
# TODO Do it by 10/10/18


class Solution:

    def flip_array(self, arr):
        n = len(arr)
        target = sum(arr)//2
        arr = sorted(arr)
        lookup = [[float('inf') for _ in range(n+1)]for _ in range(target+1)]
        for i in range(n+1):
            lookup[0][i] = 0
        for i in range(1, target+1):
            for j in range(1, n+1):
                if arr[j-1] <= i:
                    lookup[i][j] = min(lookup[i][j-1], lookup[i-arr[j-1]][j-1] + 1)
                else:
                    lookup[i][j] = lookup[i][j-1]
        res, i = None, target
        while res == None:
            if lookup[i][-1] != float('inf'):
                res = lookup[i][-1]
            i -= 1
        return res






s = Solution()
ar = [8, 4, 5, 7, 6, 2]
print(s.flip_array(ar))
