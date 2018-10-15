"""
Given 2 non negative integers m and n, find gcd(m, n)

GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
Both m and n fit in a 32 bit signed integer.

Example

m : 6
n : 9

GCD(m, n) : 3
"""

class Solution:

    def gcd(self, m, n):

        if not m or not n:
            return
        if m==n:
            return m

        if m > n:
            return self.gcd(m-n, n)
        return self.gcd(n,n-m)

    def method_2(self, m, n):

        if not m:
            return n
        return self.gcd(n%m, m)

    # def method_03(self, m, n):

s = Solution()
print(s.gcd(6,9))
