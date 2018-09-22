"""
Given two sorted integer arrays A and B, merge B into A as one sorted array.

 Note: You have to modify the array A to contain the merge of A and B. Do not output anything in your code.
TIP: C users, please malloc the result into a new array and return the result.
If the number of elements initialized in A and B are m and n respectively, the resulting size of array A after your
code is executed should be m + n

Example :

Input :
         A : [1 5 8]
         B : [6 9]

Modified A : [1 5 6 8 9]
"""


class Solution:
    def insert(self, arr, pos, k):
        temp = arr[pos]
        arr[pos] = k
        for i in range(pos + 1, len(arr)):
            p = arr[i]
            arr[i] = temp
            temp = p
        return arr

    def merge(self, a, b):
            i = 0
            j = 0
            n, m = len(a), len(b)
            a.extend([None] * m)
            while i < m + n and j < m and a[i] is not None:

                if a[i] < b[j]:
                    i += 1
                else:
                    self.insert(a, i, b[j])
                    j += 1

            while j < m:
                a[i] = b[j]
                i += 1
                j += 1

            return a


s = Solution()
a = [-4, -3, 0]
b = [2]
print(s.merge(a, b))

