"""
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.

Note that even though we want you to return the new length, make sure to change the original array as well in place

Do not allocate extra space for another array, you must do this in place with constant memory.

 Example:
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].
"""


class Solution:
    def remove_duplicate(self, arr):

        i = 0

        while i < len(arr) - 1:
            j = i + 1
            if arr[i] < arr[j]:
                i += 1
            elif arr[i] == arr[j]:
                arr.pop(i)
        return len(arr)

    def remove_duplicate_2(self, arr):
        # fast
        l = 0
        for i in range(len(arr)):
            if arr[l] != arr[i]:
                l += 1
                arr[l] = arr[i]
        return l + 1


ar = [1, 1, 1]
s = Solution()
print(s.remove_duplicate(ar))
