"""
Given an array and a value, remove all the instances of that value in the array.
Also return the number of elements left in the array after the operation.
It does not matter what is left beyond the expected length.

 Example:
If array A is [4, 1, 1, 2, 1, 3]
and value elem is 1,
then new length is 3, and A is now [4, 2, 3]
Try to do it in less than linear additional space complexity

"""

class Solution:

    def remove_element(self, arr, k):

        n = len(arr)
        count = 0
        for i in range(n):
            if arr[i] == k:
                continue
            else:
                arr[count] = arr[i]
                count += 1

        if count == 0:
            if arr[0] == k:
                return 0
            else:
                return len(arr[:count + 1])
        else:
            return len(arr[:count])


s = Solution()
a = [1,2,5,1]
k = 1
print(s.remove_element(a, k))
