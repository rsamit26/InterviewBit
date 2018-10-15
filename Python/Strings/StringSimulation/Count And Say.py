"""
The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11.
11 is read off as two 1s or 21.

21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Example:

if n = 2,
the sequence is 11.
"""


class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, n):
        countAndSayList = ["1", "11"]
        while len(countAndSayList) < n:
            countAndSayList.append("0")

        if (n <= 1):
            return countAndSayList[n]

        for j in range(2, n):
            temp = countAndSayList[j - 1]
            count = 1
            s = ""
            for i in range(1, len(temp)):
                if temp[i - 1] == temp[i]:
                    count += 1
                else:
                    s += str(count) + temp[i - 1]
                    count = 1
            s += str(count) + temp[i]
            countAndSayList[j] = s

        return countAndSayList[n - 1]
