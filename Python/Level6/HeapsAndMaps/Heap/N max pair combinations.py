"""
Given two arrays A & B of size N each.
Find the maximum n elements from the sum combinations (Ai + Bj) formed from elements in array A and B.

For example if A = [1,2], B = [3,4], then possible pair sums can be 1+3 = 4 , 1+4=5 , 2+3=5 , 2+4=6
and maximum 2 elements are 6, 5

Example:

N = 4
a[]={1,4,2,3}
b[]={2,5,1,6}

Maximum 4 elements of combinations sum are
10   (4+6),
9    (3+6),
9    (4+5),
8    (2+6)
"""


class Solution:

    def max_sum_comb(self, nums1, nums2, k, ):
        import heapq
        heap = []
        for n1 in nums1:
            for n2 in nums2:
                if len(heap) < k:
                    heapq.heappush(heap, (-n1 - n2, [n1, n2]))
                else:
                    if heap and -heap[0][0] > n1 + n2:
                        heapq.heappop(heap)
                        heapq.heappush(heap, (-n1 - n2, [n1, n2]))
                    else:
                        break
        return [heapq.heappop(heap)[1] for _ in range(k) if heap]


s = Solution()

a = [1, 4, 2, 3]
b = [2, 5, 1, 6]
k = 4
print(s.max_sum_comb(a, b, k))
