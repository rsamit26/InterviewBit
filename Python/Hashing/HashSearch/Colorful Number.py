"""
For Given Number N find if its COLORFUL number or not

Return 0/1

COLORFUL number:

A number can be broken into different contiguous sub-subsequence parts.
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
Example:

N = 23
2 3 23
2 -> 2
3 -> 3
23 -> 6
this number is a COLORFUL number since product of every digit of a sub-sequence are different.

Output : 1
"""


class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, n):
        temp = []
        hashlist = {}
        s = str(n)
        for i in range(len(s)):
            for j in range(i, len(s)):
                temp.append(s[i:j + 1])

        for l in range(len(temp)):
            mx = 1
            p = temp[l]
            for k in range(len(p)):
                mx *= int(p[k])
            hashlist[p] = mx

        temp0 = []

        for k, v in hashlist.items():
            if v not in temp0:
                temp0.append(v)
        if len(temp0) == len(temp):
            return 1
        else:
            return 0
