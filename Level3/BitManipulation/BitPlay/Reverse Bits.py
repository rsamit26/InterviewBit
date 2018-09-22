"""
Reverse bits of an 32 bit unsigned integer

Example 1:

x = 0,

          00000000000000000000000000000000
=>        00000000000000000000000000000000
return 0

Example 2:
x = 3,

          00000000000000000000000000000011
=>        11000000000000000000000000000000
return 3221225472
"""


class Solution:
    def reverse_bits(self, n):
        get_bin = lambda x, p: format(x, 'b').zfill(p)

        a = str(get_bin(n, 32))
        return int(a[::-1], 2)


s = Solution()
print(s.reverse_bits(3))
