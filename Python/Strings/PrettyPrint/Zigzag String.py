"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
rows like this: (you may want to display this pattern in a fixed font for better
legibility)

P.......A........H.......N
..A..P....L....S....I...I....G
....Y.........I........R
And then read line by line: PAHNAPLSIIGYIR
Write the code that will take a string and make this conversion given a number
of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
**Example 2 : **
ABCD, 2 can be written as

A....C
...B....D
and hence the answer would be ACBD.
"""

class Solution:

    def zigzag(self, s, r):

        n = len(s)
        if n < 2 or r == 1:
            return s
        cycle = 2*r - 2
        res = ""
        for i in range(r):
            for j in range(0, n-i, cycle):
                res += s[j+i]
                if i!= 0 and i != r-1 and j+cycle-i < n:
                    res+= s[j+cycle-i]
        return res
