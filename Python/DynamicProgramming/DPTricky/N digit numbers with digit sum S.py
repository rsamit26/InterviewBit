"""
Find out the number of N digit numbers, whose digits on being added equals to a
given number S. Note that a valid number starts from digits 1-9 except the
number 0 itself. i.e. leading zeroes are not allowed.

Since the answer can be large, output answer modulo 1000000007

**

N = 2, S = 4
Valid numbers are {22, 31, 13, 40}
Hence output 4.
"""

class Solution:

    def twoSum(self, n, s):
        lookup = {}
