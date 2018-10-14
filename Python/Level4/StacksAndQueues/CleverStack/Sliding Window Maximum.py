"""
A long array A[] is given to you. There is a sliding window of size w which is moving from the very left of the array
to the very right. You can only see the w numbers in the window. Each time the sliding window moves rightwards by one
position. You have to find the maximum for each window. The following example will give you more clarity.

Example :

The array is [1 3 -1 -3 5 3 6 7], and w is 3.

Window position	Max

[1 3 -1] -3 5 3 6 7	3
1 [3 -1 -3] 5 3 6 7	3
1 3 [-1 -3 5] 3 6 7	5
1 3 -1 [-3 5 3] 6 7	5
1 3 -1 -3 [5 3 6] 7	6
1 3 -1 -3 5 [3 6 7]	7
Input: A long array A[], and a window width w
Output: An array B[], B[i] is the maximum value of from A[i] to A[i+w-1]
Requirement: Find a good optimal way to get B[i]

 Note: If w > length of the array, return 1 element with the max of the array.
"""

class Solution:

    def largestElementInWindow(self, arr, w):
        n = len(arr)
        # from collections import defaultdict
        # lookup = defaultdict(int)
        if w >= n:
            return [max(arr)]
        res = []
        for i in range(n-w+1):
            res.append(max(arr[i:i+w]))
        return res

    def method_02(self, arr, w):
        n = len(arr)
        from collections import deque
        lookup = deque()
        if w >= n:
            return [max(arr)]
        res = []
        for i in range(n):
            while lookup and arr[i] >= arr[lookup[-1]]:
                lookup.pop()
            lookup.append(i)
            if i >= w and lookup and lookup[0] == i - w:
                lookup.popleft()
            if i >= w -1:
                res.append(arr[lookup[0]])
        return res
s = Solution()
import time
ar = [1, 3, -1, -3, 5, 3, 6, 7]
# start_time = time.time()
print(s.largestElementInWindow(ar, 80))
# print("--- %s seconds ---" % (time.time() - start_time))
# start_time = time.time()
print(s.method_02(ar, 3))
# print("--- %s seconds ---" % (time.time() - start_time))
