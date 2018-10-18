"""
Find if Given number is power of 2 or not.
More specifically, find if given number can be expressed as 2^k where k >= 1.

Input:

number length can be more than 64, which mean number can be greater than 2 ^ 64
(out of long long range)
Output:

return 1 if the number is a power of 2 else return 0

Example:

Input : 128
Output : 1
"""

class Solution:

    def powerOfTwo(self, n):
        n = int(n)
        if n == 1 or n==0:
            return 0
        elif n and n & n-1:
            return 0
        else:
            return 1
    def isPowerOfTwo(self, n):
        n = int(n)
        if n == 0:
            return 0
        while n != 1:
            if n%2 != 0:
                return 0
            n //=2
        return 1

    def method_02(self, n):
        n = int(n)
        import math
        if n == 1:
            return 0
        return int(n >0 and (math.log(n)/math.log(2)).is_integer())


s = Solution()
print(s.powerOfTwo(0))
print(s.method_02(32))
