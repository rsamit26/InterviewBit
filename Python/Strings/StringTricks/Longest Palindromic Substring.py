"""
Given a string S, find the longest palindromic substring in S.

Substring of string S:

S[i...j] where 0 <= i <= j < len(S)

Palindrome string:

A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.

Incase of conflict, return the substring which occurs first ( with the least starting index ).

Example :

Input : "aaaabaaa"
Output : "aaabaaa"
"""

class Solution:
    # Method 01 :: Using string reverse function
    def longestSubstring(self, s):
        n = len(s)

        if n < 2 or s == s[::-1]:
            return s

        longest_sq, start = 1, 0

        for i in range(1, n):
            odd = s[i-longest_sq -1 : i+1]
            even = s[i -longest_sq : i+1]

            if i-longest_sq -1 >= 0 and odd == odd[::-1]:
                start = i - longest_sq -1
                longest_sq += 2
                continue
            if i-longest_sq >= 0 and even == even[::-1]:
                start = i -longest_sq
                longest_sq += 1
        return s[start: start+longest_sq]

    # Method 02 :: Looping for every char to check if they are equal or not
    def longestPalindrome(self, s):
        n = len(s)
        if n < 2 or s == s[::-1]:
            return s
        start, low, high, maxlen = 0,0,0,1

        for i in range(1, n):
            # working on odd len palindrome
            low, high = i-1, i
            while (low >= 0 and high < n) and (s[low] == s[high]):
                if high -low +1 > maxlen:
                    start = low
                    maxlen = high - low + 1
                high += 1
                low -= 1
            # working on even palindrome string
            low, high = i-1, i+1
            while (low >= 0 and high < n) and s[low] == s[high]:
                if high - low + 1 > maxlen:
                    maxlen = high - low + 1
                    start = low
                high += 1
                low -= 1
        return s[start: start+ maxlen]

s = Solution()
print(s.longestSubstring("aaaabaaa"))
print(s.longestPalindrome("abax"))
