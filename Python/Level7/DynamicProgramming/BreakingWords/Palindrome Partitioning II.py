"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example :
Given
s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""


class Solution:

    def plindrome_partitioning_ii(self, s):

        n = len(s)

        # Create a memo_table to store minimum number of cuts
        memo_table = [0] * n

        # if s[i....j] is palindrome then is_palindrome[i][j] = 1 else 0
        is_palindrome = [[0 for _ in range(n)] for _ in range(n)]  # initializing with 0 value

        for i in range(n):
            is_palindrome[i][i] = 1  # for a single letter in string set is_palindrome to true

        for i in range(2, n + 1):  # Now loop through the substring of length of 2 ro n

            for j in range(n - i + 1):

                k = i + j - 1

                if i == 2:  # if len of substring is 2 then check only for both element is equal or not
                    if s[j] == s[k]:
                        is_palindrome[j][k] = 1
                else:  # check for corner latter and check middle part form is_palindrome table
                    if s[j] == s[k] and is_palindrome[j + 1][k - 1]:
                        is_palindrome[j][k] = 1
        for i in range(n):
            if is_palindrome[0][i]:
                memo_table[i] = 0
            else:
                import sys
                memo_table[i] = sys.maxsize

                for j in range(i):
                    if is_palindrome[j + 1][i] and (1 + memo_table[j] < memo_table[i]):
                        memo_table[i] = memo_table[j] + 1

        return memo_table[n - 1]


if __name__ == '__main__':
    c = Solution()
    s = "aab"
    print(c.plindrome_partitioning_ii(s))
