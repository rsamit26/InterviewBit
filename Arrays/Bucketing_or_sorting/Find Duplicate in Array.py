"""
Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.

Sample Input:

[3 4 1 4 1]
Sample Output:

1
If there are multiple possible answers ( like in the sample case above ), output any one.

If there is no duplicate, output -1
"""


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, arr):
        n = len(arr)
        m = max(arr)
        temp = [0] * (m + 1)

        for i in arr:
            temp[i] += 1
        for j in range(m+1):
            if temp[j] > 1:
                return j
        return -1

"""
Testing Code
"""
s = Solution()
arr = [2, 1, 3]
print(s.repeatedNumber(arr))

