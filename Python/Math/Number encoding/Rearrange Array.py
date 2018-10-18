"""
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

Example:

Input : [1, 0]
Return : [0, 1]
 Lets say N = size of the array. Then, following holds true :
All elements in the array are in the range [0, N-1]
N * N does not overflow for a signed integer
"""

class Solution:

    def rearrangeArray(self, arr):
        n = len(arr)
        for i in range(0, n):
            arr[i] += (arr[arr[i]] % n)*n

        for i in range(n):
            arr[i] = arr[i]//n


        return arr

    def method_02(self, arr):
        res = [0]*(len(arr))

        for i in range(len(arr)):
            res[i] = arr[arr[i]]
        for i in range(len(arr)):
            arr[i] = res[i]
        return arr
s = Solution()
a = [3, 2, 0, 1]
b = [1,0]
print(s.rearrangeArray(a))
print(s.method_02(b))
