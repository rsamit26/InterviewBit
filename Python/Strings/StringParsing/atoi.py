"""
Implement atoi to convert a string to an integer.

Example :

Input : "9 2704"
Output : 9
Note: There might be multiple corner cases here. Clarify all your doubts using “See Expected Output”.

 Questions: Q1. Does string contain whitespace characters before the number?
A. Yes Q2. Can the string have garbage characters after the number?
A. Yes. Ignore it. Q3. If no numeric character is found before encountering garbage characters, what should I do?
A. Return 0. Q4. What if the integer overflows?
A. Return INT_MAX if the number is positive, INT_MIN otherwise.
"""

class Solution:

    def atoi(self, string):
        INT_MAX, INT_MIN, result =  2147483647, -2147483648, 0

        if not string:
            return result

        i = 0
        while i < len(string) and string[i].isspace():
            i+=1
        print(i)

        if len(string) == i:
            return result

        sign = 1

        if string[i] == "+":
            i+= 1
        elif string[i] == "-":
            sign = -1
            i+=1

        while i < len(string) and "0" <= string <="9":
            if result > (INT_MAX - int(string[i]))/10:
                return INT_MAX if sign > 0 else INT_MIN
            result = result*10 + int(string[i])
            i+= 1
        return sign*result

s = Solution()
string = ""
print(s.atoi(string))
