"""
Determine whether an integer is a palindrome. Do this without extra space.

A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
Negative numbers are not palindromic.

Example :

Input : 12121
Output : True

Input : 123
Output : False
"""

class Solution:

    def palindromeNumber(self, n):

        if n < 0:
            return False
        else:
            n = str(n)
            return n == n[::-1]

    def method_02(self, n):
        r, o = 0, n
        if n < 0:
            return 0
        else:
            while(n > 0):
                r = r*10 + (n%10)
                n //=10
            print(r)
            if r == o:
                return 1
            else:
                return 0




s = Solution()
print(s.palindromeNumber(12121))
print(s.method_02(12121))
