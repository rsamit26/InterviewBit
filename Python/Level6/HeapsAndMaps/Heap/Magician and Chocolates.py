"""
Given N bags, each bag contains Ai chocolates. There is a kid and a magician. In one unit of time, kid chooses a
random bag i, eats Ai chocolates, then the magician fills the ith bag with floor(Ai/2) chocolates.

Given Ai for 1 <= i <= N, find the maximum number of chocolates kid can eat in K units of time.

For example,

K = 3
N = 2
A = 6 5

Return: 14
At t = 1 kid eats 6 chocolates from bag 0, and the bag gets filled by 3 chocolates
At t = 2 kid eats 5 chocolates from bag 1, and the bag gets filled by 2 chocolates
At t = 3 kid eats 3 chocolates from bag 0, and the bag gets filled by 1 chocolate
so, total number of chocolates eaten: 6 + 5 + 3 = 14

Note: Return your answer modulo 10^9+7
"""


class Solution:

    def magician_and_chocolates(self, k, arr):
        import heapq as hq

        heap = []
        for i in arr:
            hq.heappush(heap, i)
        if not heap:
            return 0
        s = 0
        d = pow(10, 9) + 7
        hq._heapify_max(heap)
        for i in range(k):
            t = hq.heappop(heap)
            print(t)
            s = (s + (t % d)) % d
            hq.heappush(heap, t // 2)
            hq._heapify_max(heap)

        return s


s = Solution()
arr = [2147483647, 2000000014, 2147483647]
print(s.magician_and_chocolates(10, arr))
