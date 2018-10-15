"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Read more details about roman numerals at Roman Numeric System

Example :

Input : "XIV"
Return : 14
Input : "XX"
Output : 20
"""

class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, s):
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        while s:
            if len(s) == 1 or val[s[0]]>=val[s[1]]:
                num += val[s[0]]
                s = s[1:]
            else:
                num += val[s[1]]-val[s[0]]
                s = s[2:]
        return num