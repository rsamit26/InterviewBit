"""
Write a function that takes an unsigned integer and returns the number of 1 bits it has.

Example:

The 32-bit integer 11 has binary representation

00000000000000000000000000001011
so the function should return 3.

"""

class Solution:

    def no_of_1_bit(self, n):

        if n == 0:
            return 0
        count =0
        while(n > 0):
            if n%2 == 1:
                count += 1
            n = n//2
        return count





s = Solution()
print(s.no_of_1_bit(14))
