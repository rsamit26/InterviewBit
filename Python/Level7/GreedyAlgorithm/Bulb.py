"""
N light bulbs are connected by a wire. Each bulb has a switch associated with it, however due to faulty wiring,
a switch also changes the state of all the bulbs to the right of current bulb. Given an initial state of all bulbs,
find the minimum number of switches you have to press to turn on all the bulbs. You can press the same switch
multiple times.

Note : 0 represents the bulb is off and 1 represents the bulb is on.

Example:

Input : [0 1 0 1]
Return : 4

Explanation :
    press switch 0 : [1 0 1 0]
    press switch 1 : [1 1 0 1]
    press switch 2 : [1 1 1 0]
    press switch 3 : [1 1 1 1]
"""


class Solution:
    # Using greedy algorithm
    # def bulbs(self, arr):
    #     n = len(arr)
    #     count = 0
    #     for i in range(n):
    #         if arr[i] == 0:
    #             count += 1
    #             arr[i] = 1
    #             for j in range(len(arr[i+1:])):
    #                 if arr[j] == 1:
    #                     arr[j] = 0
    #                 elif arr[j] == 0:
    #                     arr[j] = 1
    #             continue
    #
    #     return count, arr

    def method_02(self, arr):
        n = len(arr)
        count = 0

        if n == 0:
            return 0

        if arr[0] == 0:
            count += 1

        for i in range(1, n):
            if arr[i] != arr[i - 1]:
                count += 1

        return count


s = Solution()
ar = [0, 1, 0]
# print(s.bulbs(ar))
print(s.method_02(ar))
