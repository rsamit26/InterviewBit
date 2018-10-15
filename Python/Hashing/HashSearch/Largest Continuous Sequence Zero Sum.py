"""
Find the largest continuous sequence in a array which sums to zero.

Example:


Input:  {1 ,2 ,-2 ,4 ,-4}
Output: {2 ,-2 ,4 ,-4}

 NOTE : If there are multiple correct answers, return the sequence which occurs first in the array.

"""


class Solution:

    def zerro_seq(self, arr):
        res = []
        final = []
        i = 1


s = Solution()
arr = [1, 2, -2, 4, -4, 9, 5, -5]
print(s.zerro_seq(arr))
