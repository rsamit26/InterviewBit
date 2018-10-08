"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed)
parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""


# TODO DO this again

class Solution:

    def longest_valid_parentheses(self, s):
        n = len(s)


s = Solution()

c = "()"

print(s.longest_valid_parentheses(c))
