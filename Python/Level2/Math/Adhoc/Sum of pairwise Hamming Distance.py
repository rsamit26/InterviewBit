"""
Hamming distance between two non-negative integers is defined as the number of positions at which the corresponding bits are different.

For example,

HammingDistance(2, 7) = 2, as only the first and the third bit differs in the binary representation of 2 (010) and 7 (111).

Given an array of N non-negative integers, find the sum of hamming distances of all pairs of integers in the array.
Return the answer modulo 1000000007.

Example

Let f(x, y) be the hamming distance defined above.

A=[2, 4, 6]

We return,
f(2, 2) + f(2, 4) + f(2, 6) +
f(4, 2) + f(4, 4) + f(4, 6) +
f(6, 2) + f(6, 4) + f(6, 6) =

0 + 2 + 1
2 + 0 + 1
1 + 1 + 0 = 8

"""


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def pairdiff(self, x, y):
        m = bin(x)
        n = bin(y)
        temp = 0
        p = max(len(m), len(n))
        q = min(len(m), len(n))
        for i in range(q):
            if m[i] != n[i]:
                temp += 1
        return temp + p - q

    def hammingDistance(self, A):
        t = 0
        for i in range(len(A)):
            for j in range(len(A)):
                t += self.pairdiff(A[i], A[j])

        return t % 1000000007


"""
Testing Code
"""

s = Solution()
print(s.hammingDistance([2, 4, 6]))

##  output = 8
