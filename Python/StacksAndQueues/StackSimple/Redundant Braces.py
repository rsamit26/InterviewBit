"""
Write a program to validate if the input string has redundant braces?
Return 0/1

0 -> NO
1 -> YES
Input will be always a valid expression

and operators allowed are only + , * , - , /

Example:

((a + b)) has redundant braces so answer will be 1
(a + (a + b)) doesn't have have any redundant braces so answer will be 0
"""


class Solution:

    def redundant_braces(self, data):
        stack = []
        ops = {"+", "-", "*", "/"}
        for item in data:
            if item == "(":
                stack.append(False)

            elif item in ops:
                if not stack:
                    continue
                stack[-1] = True
            elif item == ")":
                if stack[-1]:
                    stack.pop()
                else:
                    return 1
        return 0


"""
Tseting Solution
"""

s = Solution()
string = "((a + ((b+c))))"
print(s.redundant_braces(string))
