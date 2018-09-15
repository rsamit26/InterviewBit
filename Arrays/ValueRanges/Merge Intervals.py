"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.

"""


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, new_interval):

        start = new_interval.start
        end = new_interval.end

        right = left = 0

        while right < len(intervals):
            if start <= intervals[right].end:
                if end < intervals[right].start:
                    print("True")
                    break
                start = min(start, intervals[right].start)
                end = max(end, intervals[right].end)
            else:
                left += 1
            right += 1

        return intervals[:left] + [Interval(start, end)] + intervals[right:]


arr = [Interval(1,2), Interval(3,6), Interval(6,7), Interval(8,10), Interval(12,16)]
new = Interval(4,9)
s = Solution()
output = s.insert(arr, new)

for i in output:
    print([i.start, i.end])
#
# """
# Solution Two
# """
#
# class Solution:
#     def check_overlap(self, x, y):
#         if min(x[1], y[1]) >= max(x[0], y[0]):
#             return True
#
#     def insert(self, arr, newarr):
#         ans = []
#         n = len(arr)
#         a, b = newarr[0], newarr[1]
#
#         if n == 0:
#             ans.append([a,b])
#             return ans
#
#         if b < arr[0][0]:
#             return [[a, b]] + arr
#
#         elif a > arr[n - 1][1]:
#             return arr + [[a, b]]
#
#         elif a <= arr[0][0] and b >= arr[n - 1][1]:
#             return [[a, b]]
#
#         # case4: if new interval lies between two interval
#         overlap = True
#
#         for i in range(len(arr)):
#             print(i)
#             overlap = self.check_overlap(arr[i], [a, b])
#
#             if not overlap:
#
#                 ans.append(arr[i])
#
#                 if i < n and arr[i - 1][1] < a < arr[i][0] and arr[i - 1][0] < b < arr[i][0]:
#                     ans.append([a, b])
#                 continue
#
#             temp = [0]*2
#             temp[0] = min(a, arr[i][0])
#             print(i)
#
#
#             while i < n and overlap:
#                 temp[1] = max(b, arr[i][1])
#
#                 if i == n - 1:
#                     overlap = False
#                 else:
#                     overlap = self.check_overlap(arr[i + 1], [a, b])
#                 i += 1
#             i -= 1
#             ans.append(temp)
#         return ans
#
#
# s = Solution()
# arr = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
# iarr = [4, 9]
#
# print(s.insert(arr, iarr))
