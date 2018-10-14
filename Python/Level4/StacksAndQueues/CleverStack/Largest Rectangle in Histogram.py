"""
Given n non-negative integers representing the histogram’s bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.

Largest Rectangle in Histogram: Example 1

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

Largest Rectangle in Histogram: Example 2

The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.
"""

class Solution:

    def largestArea(self, arr):
        n = len(arr)
        i = 0
        curr = 0
        largest_area = 0
        stack = []
        while i < n:

            if not stack or arr[stack[-1]] <= arr[i]:
                stack.append(i)
                i+= 1
            else:
                top = stack[-1]
                stack.pop()

                if not stack:
                    curr = arr[top]*i
                else:
                    curr = arr[top]*(i-stack[-1]-1)
                if curr > largest_area:
                    largest_area = curr
        while stack:
            top = stack[-1]
            stack.pop()
            if not stack:
                curr = arr[top]*i
            else:
                curr = arr[top]*(i-stack[-1]-1)
            if curr > largest_area:
                largest_area = curr
        return largest_area

s= Solution()
a = [6,2,5,3,12,7,8,6,9]
print(s.largestArea(a))
