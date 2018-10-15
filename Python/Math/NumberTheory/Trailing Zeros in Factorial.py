"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Example :

n = 5
n! = 120
Number of trailing zeros = 1
So, return 1
"""

class Solution:
    def trailingZeros(self, n):
        zeros=0
        mul = 5
        if n < 5:
            return 0
        else:
            while n//mul > 0:
                zeros+= n//mul
                mul *= 5
        return zeros

s = Solution()
print(s.trailingZeros(5))
