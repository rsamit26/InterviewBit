"""
Given three prime number(p1, p2, p3) and an integer k. Find the first(smallest) k integers which have only p1, p2, p3
or a combination of them as their prime factors.

Example:

Input :
Prime numbers : [2,3,5]
k : 5

If primes are given as p1=2, p2=3 and p3=5 and k is given as 5, then the sequence of first 5 integers will be:

Output:
{2,3,4,5,6}

Explanation :
4 = p1 * p1 ( 2 * 2 )
6 = p1 * p2 ( 2 * 3 )

Note: The sequence should be sorted in ascending order
"""


# TODO Do this for noraml ugly number
class Solution:

    def prime_number(self, arr, n):
        arr.sort()
        k = len(arr)
        ugly, lookup, index, ugly_nums = 1, [1], [0] * k, [1] * k
        for i in range(1, n + 1):
            for j in range(0, k):
                if ugly_nums[j] == ugly:
                    ugly_nums[j] = lookup[index[j]] * arr[j]
                    index[j] += 1
            ugly = min(ugly_nums)
            lookup.append(ugly)
        return lookup[1:]


s = Solution()
p = [2, 3, 5]
print(s.prime_number(p, 5))
