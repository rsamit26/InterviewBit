"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB

"""


class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, n):
        s = ''

        d = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M',
             13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
             25: 'Z'}

        while n > 0:
            s += d[(n - 1) % 26]
            n = (n - 1) // 26

        return s[::-1]


s = Solution()

print(s.convertToTitle(703))

# output :: 'AAA'
