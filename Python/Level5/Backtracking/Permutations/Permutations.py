"""
Given a collection of numbers, return all possible permutations.

Example:

[1,2,3] will have the following permutations:

[1,2,3]
[1,3,2]
[2,1,3]
[2,3,1]
[3,1,2]
[3,2,1]

 NOTE
No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection are unique.

"""


class Solution:

    def permutation(self, arr):
        res = []
        l = 0
        r = len(arr) - 1

        self.permutation_helper(arr, res, l, r)

        return res

    def permutation_helper(self, arr, res, l, r):

        if l == r:
            res.append(arr[:])

        else:
            for i in range(l, r + 1):
                arr[l], arr[i] = arr[i], arr[l]
                self.permutation_helper(arr, res, l + 1, r)
                arr[l], arr[i] = arr[i], arr[l]


s = Solution()

ar = [1,2,3]
print(s.permutation(ar))
