"""
Divide two integers without using multiplication, division and mod operator.

Return the floor of the result of the division.

Example:

5 / 2 = 2
Also, consider if there can be overflow cases. For overflow case, return INT_MAX
"""


class Solution:
    def devide_int(self, x, y):
        positive = (x < 0) is (y < 0)
        x, y = abs(x), abs(y)
        res = 0
        while x >= y:
            temp, i = y, 1
            while x >= temp:
                x -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

s = Solution()

print(s.devide_int(-2147483648, -1))
