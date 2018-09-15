"""
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

NOTE A solution will always exist. read Goldbach’s conjecture

Example:


Input : 4
Output: 2 + 2 = 4

If there are more than one solutions possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b,
and [c,d] is another solution with c <= d, then

[a, b] < [c, d]

If a < c OR a==c AND b < d.
"""


class Solution:
    # @param A : integer
    # @return a list of integers
    def generatePrime(self, n):
        prime = [1] * (n + 1)
        p = 2
        while p * p < n:
            if prime[p]:
                for i in range(p * 2, n + 1, p):
                    prime[i] = False
            p += 1

        c = []
        for p in range(2, n):
            if prime[p]:
                c.append(p)
        return c

    def primesum(self, A):
        p = self.generatePrime(A)
        for i in range(len(p)):
            for j in range(len(p)):
                if p[i] + p[j] == A:
                    return [p[i], p[j]]


"""Testing Code"""
s = Solution()
print(s.primesum(4))

# output == [2,2]
