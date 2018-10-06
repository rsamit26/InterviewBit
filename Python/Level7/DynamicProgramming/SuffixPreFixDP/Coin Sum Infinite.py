"""
You are given a set of coins S. In how many ways can you make sum N assuming you have infinite amount of each coin in
the set.

Note : Coins in set S will be unique. Expected space complexity of this problem is O(N).

Example :

Input :
S = [1, 2, 3]
N = 4

Return : 4

Explanation : The 4 possible ways are
{1, 1, 1, 1}
{1, 1, 2}
{2, 2}
{1, 3}
Note that the answer can overflow. So, give us the answer % 1000007

"""


# TODO DO this using Recursion


class Solution:

    def coin_sum(self, coins_set, target):
        n = len(coins_set)
        memo_table = [0] * (target + 1)  # Memo Table to store no of solution for each target sum

        memo_table[0] = 1  # Base Case :: for getting target sum 0 we have 1 solution the don't take any coin

        for i in range(n):
            for j in range(coins_set[i], target + 1):
                memo_table[j] += memo_table[j - coins_set[i]]

        return memo_table[target] % 1000007

    def method_02(self, coin_set, target):
        n = len(coin_set)
        if not target:  # if target is zero then only one solution -- do not take any coin
            return 1

        """ if target is negative or (coin set is empty and target is positive natural number) then no solution """
        if (not coin_set and target >= 1) or target < 0:
            return 0

        return self.method_02(coin_set[: n - 1], target) + self.method_02(coin_set, target - coin_set[n - 1])


s = Solution()
c = [1, 2, 3]
print(s.coin_sum(c, 20))
