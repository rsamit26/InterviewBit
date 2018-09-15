"""
Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

Example

Input : 4
Output : True
as 2^2 = 4.
"""

import math


class Solution:
    # @param A : integer
    # @return an integer

    def isPower(self, A):
        if A == 1:
            return 1
        for x in range(2, int(math.sqrt(A)) + 1):
            y = 2
            p = int(math.pow(x, y))
            while A >= p > 0:
                if p == A:
                    return 1

                y = y + 1
                p = math.pow(x, y)
        return 0

"""
Testing Code
"""

s = Solution()
print(s.isPower(144))

# output :: 1 ~ True
