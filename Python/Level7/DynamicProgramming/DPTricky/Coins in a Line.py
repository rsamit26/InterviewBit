"""
There are N coins (Assume N is even) in a line. Two players take turns to take a coin from one of the ends of the line
until there are no more coins left. The player with the larger amount of money wins. Assume that you go first.

Write a program which computes the maximum amount of money you can win.

Example:

suppose that there are 4 coins which have value
1 2 3 4
now you are first so you pick 4
then in next term
next person picks 3 then
you pick 2 and
then next person picks 1
so total of your money is 4 + 2 = 6
next/opposite person will get 1 + 3 = 4
so maximum amount of value you can get is 6
"""


class Solution:

    def max_coin(self, coins):
        if not coins:
            return 0

        n = len(coins)
        a, b, c = 0, 0, 0

        memo_table = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for k, j in enumerate(range(i, n)):
                if k + 2 <= n - 1:
                    a = memo_table[k + 2][j]

                if k + 1 <= n - 1 and j - 1 >= 0:
                    b = memo_table[k + 1][j - 1]

                if j - 2 >= 0:
                    c = memo_table[k][j - 2]

                memo_table[k][j] = max(coins[k] + min(a, b), coins[j] + min(b, c))
        return memo_table[0][n - 1]

    def max_coin_02(self, coins):
        n = len(coins)
        memo_table = [0] * n

        for j in range(1, n + 1):
            memo_table[j - 1] = coins[j - 1]  # dp[j-1][j]
            total = coins[j - 1]
            for i in range(j - 2, -1, -1):
                total += coins[i]  # sum[i:j]
                memo_table[i] = total - min(memo_table[i + 1], memo_table[i])

        return memo_table[0]


s = Solution()
c = [2, 3, 1, 5]
print(s.max_coin(c))
