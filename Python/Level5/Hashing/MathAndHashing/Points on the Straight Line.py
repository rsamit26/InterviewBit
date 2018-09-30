"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Sample Input :

(1, 1)
(2, 2)
Sample Output :

2
You will be give 2 arrays X and Y. Each point is represented by (X[i], Y[i])
"""


class Solutin:

    def point_on_st_line(self, x, y):
        from collections import defaultdict
        points = []
        for i in range(len(x)):
            points.append([x[i], y[i]])

        max_point = 0

        for i, start in enumerate(points):
            slope_count, same = defaultdict(int), 1
            for j in range(i + 1, len(points)):
                end = points[j]
                if start[0] == end[0] and start[1] == end[1]:
                    same += 1
                else:
                    slope = float("inf")
                    if start[0] - end[0] != 0:
                        slope = (start[1] - end[1]) * 1.0 / (start[0] - end[0])
                    slope_count[slope] += 1

            curr_max = same
            for slope in slope_count:
                curr_max = max(curr_max, slope_count[slope] + same)

            max_point = max(max_point, curr_max)

        return max_point


s = Solutin()
a = [0, 1, -1]
b = [0, 1, -1]
print(s.point_on_st_line(a, b))
