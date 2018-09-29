"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate
numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

 Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The combinations themselves must be sorted in ascending order.
CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR … (a1 = b1 AND a2 = b2 AND … ai = bi AND
ai+1 > bi+1)
The solution set must not contain duplicate combinations.
Example,
Given candidate set 2,3,6,7 and target 7,
A solution set is:

[2, 2, 3]
[7]
 Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
Example : itertools.combinations in python.
If you do, we will disqualify your submission retroactively and give you penalty points.
"""


class Solution:

    def comb_sum_helper(self, candidate, target, curr, result, i):
        n = len(candidate)

        if target < 0:
            return
        if target == 0:
            result.append(curr[:])
            return

        while i < n and target - candidate[i] >= 0:
            curr.append(candidate[i])
            self.comb_sum_helper(candidate, target - candidate[i], curr, result, i)
            i += 1
            curr.pop()

    def combination_sum(self, candidate, target):

        curr = []

        for i in candidate:
            if i not in curr:
                curr.append(i)
        curr.sort()
        candidate = curr
        curr = []
        result = []
        self.comb_sum_helper(candidate, target, curr, result, 0)
        return result


s = Solution()
c = [2, 4, 6, 8]
t = 8
print(s.combination_sum(c, t))
