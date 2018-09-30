"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example :

Given numerator = 1, denominator = 2, return "0.5"
Given numerator = 2, denominator = 1, return "2"
Given numerator = 2, denominator = 3, return "0.(6)"
"""


class Solution:

    def fraction(self, num, den):

        if not num:
            return "0"
        result = ""

        if (num > 0 > den) or (num < 0 < den):
            result = "-"  # if any of numerator or denominator is negative starting final string with (-) negative sign

        n, d = abs(num), abs(den)

        result += str(n // d)  # adding Quotient to final string

        r = n % d  # remainder

        if r > 0:
            result += "."  # if remainder then add decimal point in final string

        hash_map = {}  # creating a hash table for storing the fractional value and location of string

        while r and r not in hash_map:
            hash_map[r] = len(result)
            r *= 10
            result += str(r // d)
            r %= d

        if r in hash_map:
            result = result[:hash_map[r]] + "(" + result[hash_map[r]:] + ")"

        return result


s = Solution()
print(s.fraction(-2147483648, -13))
