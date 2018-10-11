"""
Given an array of integers, return the highest product possible by multiplying 3 numbers from the array

Input:

array of integers e.g {1, 2, 3}
 NOTE: Solution will fit in a 32-bit signed integer
Example:

[0, -1, 3, 100, 70, 50]

=> 70*50*100 = 350000
"""


class Solution:

    # T = O(nlogn)
    def highest_product(self, arr):
        arr.sort()
        n = len(arr)
        return max(arr[0] * arr[1] * arr[n - 1], arr[n - 1] * arr[n - 2] * arr[n - 3])

    # T = O(n)
    def method_02(self, arr):

        if len(arr) < 3:
            return 0
        import sys
        min1 = min2 = sys.maxsize
        max1 = max2 = max3 = -sys.maxsize
        for item in arr:

            if item > max1:
                max3 = max2
                max2 = max1
                max1 = item
            elif item > max2:
                max3 = max2
                max2 = item
            elif item > max3:
                max3 = item

            if item < min1:
                min2 = min1
                min1 = item
            elif item < min2:
                min2 = item

        return max(min1 * min2 * max1, max1 * max2 * max3)


s = Solution()
ar = [-10000000, 1, 2, 3, 4]

print(s.highest_product(ar))
print(s.method_02(ar))
