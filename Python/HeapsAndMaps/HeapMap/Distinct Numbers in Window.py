"""
You are given an array of N integers, A1, A2 ,…, AN and an integer K. Return the of count of distinct numbers in all
windows of size K.

Formally, return an array of size N-K+1 where i’th element in this array contains number of distinct elements in
sequence Ai, Ai+1 ,…, Ai+k-1.

Note:

If K > N, return empty array.
For example,

A=[1, 2, 1, 3, 4, 3] and K = 3

All windows of size K are

[1, 2, 1]
[2, 1, 3]
[1, 3, 4]
[3, 4, 3]

So, we return an array [2, 3, 3, 2].
"""


class Solution:

    def snums(self, arr, k):

        n = len(arr)

        if k > n or k == 0:
            return []
        result = []

        for i in range(n - k + 1):
            temp = []
            for i in arr[i:i + k]:
                if i not in temp:
                    temp.append(i)

            result.append(len(temp))

        return result

    def method_02(self, arr, k):
        """
        lookup :: hash table for storing count of element in windows
        result :: list to store the no of distinct no in ith window
        count :: counter to count no of distinct item in window

        """
        from collections import defaultdict
        n = len(arr)
        if k > n or k == 0:  # Corner Case
            return []
        lookup = defaultdict(int)
        result = []
        count = 0

        # for first window we are creating lookup table and counting no of distinct item.
        for i in range(k):
            if not lookup[arr[i]]:
                lookup[arr[i]] = 1
                count += 1
            else:
                lookup[arr[i]] += 1

        result.append(count)

        for i in range(k, n):
            # check if the occurrence of 0th item of the first window is one the remove the item and/
            # decrease the distinct counter by 1 ;; else just decrease the occurrence of item by 1/
            # in lookup table.
            if lookup[arr[i - k]] == 1:
                lookup.pop(arr[i - k])
                count -= 1
            else:
                lookup[arr[i - k]] -= 1

            if not lookup[arr[i]]:
                lookup[arr[i]] = 1
                count += 1
            else:
                lookup[arr[i]] += 1
            result.append(count)

        return result


s = Solution()
a = [1, 2, 1, 3, 4, 3]
print(s.snums(a, 3))
print(s.method_02(a, 3))
