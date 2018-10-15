"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example :

Input : 3
Return : 3

Steps : [1 1 1], [1 2], [2 1]
"""


class Solution:

    def stairs(self, n):
        # Corner Case
        if n == 0:
            return 0

        # Memo table to store no of ways to climb any stair i
        memo_table = [0] * (n + 1)

        # Base Case
        memo_table[0] = 1  # There are 1 ways to climb the first stair
        memo_table[1] = 2  # There are two ways to climb the 2nd Stair -> (1,1) or (2)

        for i in range(2, n + 1):
            memo_table[i] = memo_table[i - 2] + memo_table[i - 1]

        return memo_table[n - 1]

    # Time O(n) space = O(1)
    def stairs_02(self, n):

        prev, nxt = 0, 1

        for _ in range(n):
            prev, nxt = nxt, prev + nxt
        return nxt


s = Solution()

print(s.stairs(20))
print(s.stairs_02(20))
