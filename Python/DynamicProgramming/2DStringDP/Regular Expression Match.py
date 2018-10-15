"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' : Matches any single character.
'*' : Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

The function prototype should be:

int isMatch(const char *s, const char *p)
Examples :

isMatch("aa","a") → 0
isMatch("aa","aa") → 1
isMatch("aaa","aa") → 0
isMatch("aa", "*") → 1
isMatch("aa", "a*") → 1
isMatch("ab", "?*") → 1
isMatch("aab", "c*a*b") → 0
"""


class Solution:

    def regex_match(self, s, p):
        p = list(p)
        stack = []
        for i in range(len(p)):
            if not stack:
                stack.append(p[i])
            elif stack[-1] == "*" and p[i] == "*":
                continue
            else:
                stack.append(p[i])

        p = "".join(stack)
        n, m = len(s), len(p)
        memo_table = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        memo_table[0][0] = 1

        for i in range(1, m + 1):
            if p[i - 1] == '*':
                memo_table[0][i] = memo_table[0][i - 1]

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if p[j - 1] == '*':
                    memo_table[i][j] = memo_table[i][j - 1] or memo_table[i - 1][j]

                elif p[j - 1] == "?" or s[i - 1] == p[j - 1]:
                    memo_table[i][j] = memo_table[i - 1][j - 1]

        return memo_table[n][m]

    def regex_match_02(self, s, p):

        n, m = len(s), len(p)

        if not n and not m:  # if both string and pattern is none then both are matching -> Return 1
            return 1

        if not m:  # if pattern is None then string will not match to None -> Return 0
            return 0

        i, j, star, curr_i = 0, 0, None, None

        while i < n:  # looping over length of string
            if j < m and (s[i] == p[j] or p[j] == '?'):
                j += 1
                i += 1
            elif j < m and p[j] == "*":
                star = j
                j += 1
                curr_i = i

            elif star is not None:
                curr_i += 1
                i = curr_i
                j = star + 1

            else:
                return 0
        while j < m and p[j] == "*":
            j += 1

        return 1 if j == m else 0


s = Solution()
p = "a**ac*babb*b"
c = "a"
print(s.regex_match(c, p))
print(s.regex_match_02(c, p))
