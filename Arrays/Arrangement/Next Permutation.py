"""
Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers.

If such arrangement is not possible, it must be rearranged as the lowest possible order ie, sorted in an ascending order.

The replacement must be in-place, do not allocate extra memory.

Examples:

1,2,3 → 1,3,2

3,2,1 → 1,2,3

1,1,5 → 1,5,1

20, 50, 113 → 20, 113, 50
"""


class Solution:
    def next_permutation(self, arr):
        n = len(arr)

        if n <= 1:
            return

        i = n - 1

        while i > 0 and arr[i] <= arr[i - 1]:
            i -= 1
        if i > 0:
            j = n - 1
            while j >= i:
                if arr[j] > arr[i - 1]:
                    arr[j], arr[i - 1] = arr[i - 1], arr[j]
                    break
                j -= 1

        m = n - 1
        while i < m:
            arr[i], arr[m] = arr[m], arr[i]
            i += 1
            m -= 1

        return arr


s = Solution()
a = [20, 50, 113]
print(s.next_permutation(a))
