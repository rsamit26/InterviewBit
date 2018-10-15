"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

Example :

Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""


class Solution:

    def ways_to_decode(self, msg):
        n = len(msg)

        if not msg or msg[0] == '0':  # Corner Case if first digit is 0 then no of ways is 0
            return 0

        # Creating Memo Table for storing sub problem decoding ways,
        # /initialising the the value of 0 and 1 len msg to 1

        memo_table = [0] * (n + 1)
        memo_table[0], memo_table[1] = 1, 1

        for i in range(2, n + 1):  # Looping from 3rd digit of message to last

            memo_table[i] = 0

            if msg[i - 1] != '0':
                memo_table[i] = memo_table[i - 1]

            if msg[i - 2] == '1' or (msg[i - 2] == '2' and msg[i - 1] < '7'):
                memo_table[i] += memo_table[i - 2]

        return memo_table[n]  # Returning the no of ways from the memo table for msg length n


s = Solution()
m = "11212131114111411111267896878678456546525462645"
print(s.ways_to_decode(m))