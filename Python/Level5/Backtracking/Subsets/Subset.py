"""
Given a set of distinct integers, S, return all possible subsets.

 Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.
Example :

If S = [1,2,3], a solution is:

[
  [],
  [1],
  [1, 2],
  [1, 2, 3],
  [1, 3],
  [2],
  [2, 3],
  [3],
]
"""


class Solution:

    def subset(self, s):
        res = self.subset_helper([], sorted(s))
        res.sort()
        return res

    def subset_helper(self, curr, s):
        print([curr])
        if s:
            return self.subset_helper(curr, s[1:]) + self.subset_helper(curr + [s[0]], s[1:])
        return [curr]


c = Solution()

s = [1, 2, 3]

print(c.subset(s))
