"""
Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.

Make sure the combinations are sorted.

To elaborate,

Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
Entries should be sorted within themselves.
Example :
If n = 4 and k = 2, a solution is:

[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4],
]
"""


class Solution:

    def combination(self, n, k):
        """  Using Recursion find all the subset the return subset with length equal to """
        arr = []
        for i in range(1, n + 1):
            arr.append(i)

        if k > n or k == 0:
            return [[]]
        elif k == n:
            return [arr]

        res = self.comb_helper([], arr)
        temp = []
        for i in res:
            if len(i) == k:
                temp.append(i)
        temp.sort()

        return temp

    def comb_helper(self, curr, arr):
        if arr:
            return self.comb_helper(curr, arr[1:]) + self.comb_helper(curr + [arr[0]], arr[1:])
        return [curr]

    def combination_02(self, n, k):
        """ Using iteration less time """
        result, combination = [], []
        i = 1
        while True:
            if len(combination) == k:
                result.append(combination[:])
            if len(combination) == k or len(combination) + (n - i + 1) < k:
                if not combination:
                    break
                i = combination.pop() + 1
            else:
                combination.append(i)
                i += 1
        return result




p = Solution()

k = 2
# print(p.combination(19, 4))
print(p.combination_02(1, 4))
