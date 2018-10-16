"""
You are given two positive numbers A and B. You need to find the maximum valued
integer X such that:

X divides A i.e. A % X = 0
X and B are co-prime i.e. gcd(X, B) = 1
For example,

A = 30
B = 12
We return
X = 5
"""

class Solution:

    def largestCoprime(self, a, b):

        for i in range(a+1, 0, -1):
            if a%i == 0:
                if self.gcd(i, b) == 1:
                    return i
                else:
                    continue

    def gcd(self, m, n):
        if not m:
            return n
        return self.gcd(n%m, m)


    def method_2(self, a, b):

        while True:
            x,y = a,b
            while y >0:
                x,y = y,x%y
            if x == 1:
                return a
            a = a//x


s = Solution()
print(s.largestCoprime(2,3))
print(s.method_2(2,3))
