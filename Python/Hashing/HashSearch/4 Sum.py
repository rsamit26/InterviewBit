"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

 Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
Example :
Given array S = {1 0 -1 0 -2 2}, and target = 0
A solution set is:

    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
    (-1,  0, 0, 1)
Also make sure that the solution set is lexicographically sorted.

Solution[i] < Solution[j] iff Solution[i][0] < Solution[j][0] OR (Solution[i][0] == Solution[j][0] AND ...
Solution[i][k] < Solution[j][k])

"""
import timeit

from collections import defaultdict


class Solution:

    def four_sum(self, arr, target):

        arr, result, has_table = sorted(arr), [], defaultdict(list)

        for i in range(0, len(arr) - 1):
            for j in range(i + 1, len(arr)):
                duplicate = False
                for [x, y] in has_table[arr[i] + arr[j]]:
                    if arr[x] == arr[i]:
                        duplicate = True
                        break
                if not duplicate:
                    has_table[arr[i] + arr[j]].append([i, j])

        curr = {}

        for k in range(2, len(arr)):
            for m in range(k + 1, len(arr)):
                if target - arr[k] - arr[m] in has_table:
                    for [a, b] in has_table[target - arr[k] - arr[m]]:
                        if b < k:
                            pairs = [arr[a], arr[b], arr[k], arr[m]]
                            pairs_temp = " ".join(str(pairs))
                            if pairs_temp not in curr:
                                curr[pairs_temp] = True
                                result.append(pairs)
        result.sort()
        return result


class Solution2:
    def four_sum(self, arr, target):
        hash_map = dict()
        arr.sort()
        result = set()

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                curr_sum = arr[i] + arr[j]
                diff = target - curr_sum
                if diff in hash_map:
                    for prev_sum in hash_map[diff]:
                        if arr[prev_sum[1]] <= arr[i] and i > prev_sum[1]:
                            result.add((arr[prev_sum[0]], arr[prev_sum[1]], arr[i], arr[j]))

                if curr_sum in hash_map:
                    hash_map[curr_sum].append((i, j))
                else:
                    hash_map[curr_sum] = [(i, j)]

        return sorted([list(item) for item in result])


start = timeit.default_timer()
s = Solution()
arr = [1, 0, -1, 0, -2, 2]
print(s.four_sum(arr, 0))
stop = timeit.default_timer()
print('Time: ', stop - start)

start = timeit.default_timer()
s2 = Solution2()
arr = [1, 0, -1, 0, -2, 2]
print(s2.four_sum(arr, 0))
stop = timeit.default_timer()
print('Time: ', stop - start)
