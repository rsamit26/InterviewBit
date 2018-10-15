# coding=utf-8
"""
There are N Mice and N holes are placed in a straight line.
Each hole can accomodate only 1 mouse.
A mouse can stay at his position, move one step right from x to x + 1, or move one step left from x to x − 1.
Any of these moves consumes 1 minute.
Assign mice to holes so that the time when the last mouse gets inside a hole is minimized.

Example:

positions of mice are:
4 -4 2
positions of holes are:
4 0 5

Assign mouse at position x=4 to hole at position x=4 : Time taken is 0 minutes
Assign mouse at position x=-4 to hole at position x=0 : Time taken is 4 minutes
Assign mouse at position x=2 to hole at position x=5 : Time taken is 3 minutes
After 4 minutes all of the mice are in the holes.

Since, there is no combination possible where the last mouse's time is less than 4,
answer = 4.
Input:

A :  list of positions of mice
B :  list of positions of holes
Output:

single integer value

"""


class Solution:

    def mice_holes(self, mice, holes):
        n = len(mice)
        mice.sort()
        holes.sort()
        max_time = 0
        for i in range(n):
            max_time = max(max_time, abs(mice[i]- holes[i]))
        return max_time



s = Solution()
m = [-10, -79, -79, 67, 93, -85, -28, -94]
h = [-2, 9, 69, 25, -31, 23, 50, 78]
print(s.mice_holes(m, h))
