"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example :
[1,1,2] have the following unique permutations:

[1,1,2]
[1,2,1]
[2,1,1]
"""


# TODO DO again using recursion


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, nums):
        perms = [[]]
        for n in nums:
            new_perm = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    new_perm.append(perm[:i] + [n] + perm[i:])
                    # handle duplication
                    if i < len(perm) and perm[i] == n: break
            perms = new_perm
        return perms
