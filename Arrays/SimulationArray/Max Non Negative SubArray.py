"""
Find out the maximum sub-array of non negative numbers from an array.
The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping
the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array
B if sum(A) > sum(B).

Example:

A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]
NOTE: If there is a tie, then compare with segment's length and return segment which has maximum length
NOTE 2: If there is still a tie, then return the segment with minimum starting index
"""


class Solution:
    def maxSet(self, arr):
        curr_sum, curr_len, curr_index = 0, 0, 0
        global_sum, global_len, global_index = 0, 0, 0,

        for i in range(len(arr)):
            if arr[i] < 0:
                if curr_sum > global_sum or (curr_sum == global_sum and curr_len > global_len):
                    global_sum, global_index, global_len = curr_sum, curr_index, curr_len
                    curr_index, curr_len, curr_sum = i + 1, 0, 0

            else:
                curr_sum += arr[i]
                curr_len += 1

        if curr_sum > global_sum or (global_sum == curr_sum and curr_len > global_len):
            global_sum, global_index, global_len = curr_sum, curr_index, curr_len

        return arr[global_index: global_index + global_len]


s = Solution()
a = [1, 2, 5, -7, 2, 3, 9, -5, 6, 4, 1, 3]
print(s.maxSet(a))
