"""
Please Note:
Another question which belongs to the category of questions which are intentionally stated vaguely.
Expectation is that you will ask for correct clarification or you will state your assumptions before you start coding.

Given an integer, convert it to a roman numeral, and return a string corresponding to its roman numeral version

Input is guaranteed to be within the range from 1 to 3999.

Example :

Input : 5
Return : "V"

Input : 14
Return : "XIV"
"""


class Solution:
    # @param A : integer
    # @return a strings
    def method_01(self, num):
        s = ""
        while num >= 1000:
            s  += 'M'
            num -= 1000
        if num >= 900:
            s += 'CM'
            num -= 900
        if num >= 500:
            s+= 'D'
            num -= 500
        if num >= 400:
            num -= 400
            s+= 'CD'
        while num >= 100:
            num -= 100
            s+= 'C'
        if num >= 90:
            num -= 90
            s+= 'XC'
        if num >= 50:
            num -= 50
            s+= 'L'
        if num >= 40:
            s+= 'XL'
            num -= 40
        while num >= 10:
            s+= 'X'
            num -= 10
        if num == 9:
            s+= 'IX'
            return s
        if num >=5:
            s+= 'V'
            num -= 5
        if num == 4:
            s+= 'IV'
            return s
        while num > 0:
            s+= 'I'
            num -= 1
        return s





    def method_02(self, num):
        num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                   (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        roman = ""
        while (num > 0):
            for i, r in num_map:
                while num >= i:
                    roman += r
                    num -= i
        return roman
