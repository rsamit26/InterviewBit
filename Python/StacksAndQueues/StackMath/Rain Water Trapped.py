"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water
it is able to trap after raining.

Example :

Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

Rain water trapped: Example 1

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
"""


# TODO Again do this using stack

class Solution:

    def rain_water_trap(self, arr):
        n = len(arr)
        result = 0

        left_max = 0
        right_max = 0

        l = 0
        r = n - 1

        while l <= r:

            if arr[l] < arr[r]:

                if arr[l] > left_max:

                    left_max = arr[l]
                else:

                    result += left_max - arr[l]
                l += 1

            else:

                if arr[r] > right_max:
                    right_max = arr[r]
                else:
                    result += right_max - arr[r]
                r -= 1

        return result


s = Solution()
dp = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(s.rain_water_trap(dp))
