"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

 Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
Example :

Given candidate set 10,1,2,7,6,1,5 and target 8,

A solution set is:

[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
 Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
Example : itertools.combinations in python.
If you do, we will disqualify your submission retroactively and give you penalty points.
"""


class Solution:

    def comb_sum_helper_ii(self, candidate, target, curr, result, start):

        if not target:
            result.append(curr)
            return

        for i in range(start, len(candidate)):
            if i > start and candidate[i] == candidate[i - 1]:
                continue
            if candidate[i] > target:
                break

            self.comb_sum_helper_ii(candidate, target - candidate[i], curr + [candidate[i]], result, i + 1)

    def combination_sum_ii(self, candidate, target):

        candidate.sort()
        result, curr = [], []
        self.comb_sum_helper_ii(candidate, target, curr, result, 0)
        result.sort()
        return result


s = Solution()
c = [10,1,2,7,6,1,5]
t = 8
print(s.combination_sum_ii(c, t))
