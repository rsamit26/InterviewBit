"""
Given an array of integers, sort the array into a wave like array and return it,
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

Example

Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]

"""


class Solution:
    def wave_aaray(self, arr):
        # O(n) Extra Space
        n = len(arr)
        arr.sort()
        temp = []
        print(arr)
        i = 1

        while i < n:
            temp.append((arr[i]))
            temp.append(arr[i - 1])
            i += 2
        if n % 2 != 0:
            temp.append(arr[-1])
        return temp

    def wave_array_01(self, arr):
        # O(1) Space
        n = len(arr)
        arr.sort()
        for i in range(0, n - 1, 2):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        return arr


"""
Running Code
"""

s = Solution()
arr = [1, 3, 2, 4, 5]
print(s.wave_aaray(arr))
print("Solution 2", s.wave_array_01(arr))
