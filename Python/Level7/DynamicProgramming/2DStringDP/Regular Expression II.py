"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:

int isMatch(const char *s, const char *p)
Some examples:

isMatch("aa","a") → 0
isMatch("aa","aa") → 1
isMatch("aaa","aa") → 0
isMatch("aa", "a*") → 1
isMatch("aa", ".*") → 1
isMatch("ab", ".*") → 1
isMatch("aab", "c*a*b") → 1
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""


# TODO -- Do this again
class Solution:

    def regex_search(self, s, p):
        k = 3
        # result = [[False for _ in range(len(p) + 1)] for _ in range(k)]
        #
        # result[0][0] = True
        # for i in range(2, len(p) + 1):
        #     if p[i - 1] == '*':
        #         result[0][i] = result[0][i - 2]
        #
        # for i in range(1, len(s) + 1):
        #     if i > 1:
        #         result[0][0] = False
        #     for j in range(1, len(p) + 1):
        #         if p[j - 1] != '*':
        #             result[i % k][j] = result[(i - 1) % k][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
        #         else:
        #             result[i % k][j] = result[i % k][j - 2] or (
        #                     result[(i - 1) % k][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
        #
        # return int(result[len(s) % k][len(p)])


s = Solution()
p = "c*a*b"
c = "aab"
print(s.regex_search(c, p))
