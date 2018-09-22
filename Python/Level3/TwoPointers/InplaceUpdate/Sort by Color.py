"""
Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: Using library sort function is not allowed.

Example :

Input : [0 1 2 0 1 2]
Modify array so that it becomes : [0 0 1 1 2 2]
"""

class Solution:

    def sort_by_color(self, arr):
        redA = []
        whiteA = []
        blueA = []

        for i in arr:
            if i == 0:
                redA.append(i)
            elif i == 1:
                whiteA.append(i)
            else:
                blueA.append(i)

        return redA + whiteA + blueA

s = Solution()
a = [0, 1, 2, 0, 1, 2]
print(s.sort_by_color(a))