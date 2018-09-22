"""
Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in place such that each element can appear atmost twice and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

Note that even though we want you to return the new length, make sure to change the original array as well in place

For example,
Given input array A = [1,1,1,2],

Your function should return length = 3, and A is now [1,1,2].
"""


class Solution:
    def remove_duplicate_2(self, arr):
        i, j, k = 0, 0, 0
        while i < len(arr) - 2:
            j = i + 1
            k = j + 1
            if arr[i] == arr[j] == arr[k]:
                arr.pop(k)
            else:
                i += 1

        return arr

    def remove_duplicates_2_02(self, arr):
        i = 0
        for n in arr:
            if i < 2 or n > arr[i - 2]:
                arr[i] = n
                i += 1
        return i

    def remove_solution_2_03(self, arr):
        if not arr:
            return 0

        last, i, same = 0, 1, False
        while i < len(arr):
            if arr[last] != arr[i] or not same:
                same = arr[last] == arr[i]
                last += 1
                arr[last] = arr[i]
            i += 1

        return last + 1


s = Solution()
a = [1, 1, 1, 1, 1, 2, 2, 4, 5, 5, 5, 5, 6]
print(s.remove_duplicates_2_02(a))
