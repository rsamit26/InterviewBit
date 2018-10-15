"""
Given a collection of integers that might contain duplicates, S, return all possible subsets.

 Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
The subsets must be sorted lexicographically.
Example :
If S = [1,2,2], the solution is:

[
[],
[1],
[1,2],
[1,2,2],
[2],
[2, 2]
]
"""


class Solution:

    def subset(self, s):
        res = self.subset_helper([], sorted(s))
        final = []
        for i in res:
            if i not in final:
                final.append(i)
        final.sort()
        return final

    def subset_helper(self, curr, s):
        if s:
            return self.subset_helper(curr, s[1:]) + self.subset_helper(curr + [s[0]], s[1:])
        return [curr]


c = Solution()

s = [2, 2]

print(c.subset(s))
