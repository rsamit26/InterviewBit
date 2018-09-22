"""
Given a collection of intervals, merge all overlapping intervals.

For example:

Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted.

"""

class Interval:
    def __init__(self, s =0, e =0 ):
        self.start = s
        self.end = e

class Solution:

    def merge(self, intervals):
        temp = []
        for i in intervals:
            temp.append([i.start, i.end])
        temp.sort()
        merged = [temp[0]]
        for current in temp:
            previous = merged[-1]
            if current[0] <= previous[1]:
                previous[1] = max(previous[1], current[1])
            else:
                merged.append(current)
        res =[]

        for i in merged:
            res.append(Interval(i[0],i[1]))

        return res

arr = [Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)]

s = Solution()

print(s.merge(arr))

