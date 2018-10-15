
"""
Reverse digits of an integer.

Example1:

x = 123,

return 321
Example2:

x = -123,

return -321

Return 0 if the result overflows and does not fit in a 32 bit signed integer
"""

class Solution:

    def reverseInteger(self, num):
        if num < 0:
            num = num * -1
            r = (int(str(num)[::-1]))
            if r < (1 << 31) -1:
                return -num
            else:
                return 0
        else:
            r = int(str(num)[::-1])
            if r < (1 << 31) -1:
                return num
            else:
                return 0
    def method_02(self, num):
        rev, ori = 0, num
        num = abs(num)
        while num > 0:
            rev = rev*10 + num%10
            num //= 10
        if rev < (1 << 31) -1:
            if ori < 0:
                return -rev
            else:
                return rev
        else:
            return 0




s = Solution()
print(s.reverseInteger(1146467285))
