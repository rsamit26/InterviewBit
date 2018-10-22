"""
Given an array with non negative numbers, divide the array into two parts such
that the average of both the parts is equal.
Return both parts (If exist).
If there is no solution. return an empty list.

Example:


Input:
[1 7 15 29 11 9]

Output:
[9 15] [1 7 11 29]

The average of part is (15+9)/2 = 12,
average of second part elements is (1 + 7 + 11 + 29) / 4 = 12

 NOTE 1: If a solution exists, you should return a list of exactly 2 lists of
integers A and B which follow the following condition :
numElements in A <= numElements in B
If numElements in A = numElements in B, then A is lexicographically smaller
than B ( https://en.wikipedia.org/wiki/Lexicographical_order )
NOTE 2: If multiple solutions exist, return the solution where length(A) is
minimum. If there is still a tie, return the one where A is lexicographically
smallest. NOTE 3: Array will contain only non negative numbers.
"""

class Solution:

    def partitionArray(self, arr):
