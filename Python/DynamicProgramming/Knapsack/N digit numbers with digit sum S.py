"""
Find out the number of N digit numbers, whose digits on being added equals to a
given number S. Note that a valid number starts from digits 1-9 except the number
0 itself. i.e. leading zeroes are not allowed.

Since the answer can be large, output answer modulo 1000000007

**

N = 2, S = 4
Valid numbers are {22, 31, 13, 40}
Hence output 4.
"""

class Solution:

    def numbers(self, n, target):

        lookup = [[-1 for _ in range(101)]for _ in range(501)]
        curr = 0
        # running loop for 1st digit Since this can't be zero
        for i in range(1,10):
            if target - i >= 0:
                curr += self.helper(lookup, n-1, target - i)
        return curr

    def helper(self, lookup, n, target):

        if n == 0:
            return (target == 0)

        if lookup[n][target] != -1:
            return lookup[n][target]

        curr = 0

        for i in range(10):
            if target -i >= 0:
                curr += self.helper(lookup, n-1, target-i)
        return curr


s = Solution()
print(s.numbers(3,5))
