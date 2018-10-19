"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example :
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

If it is not possible to reach the end index, return -1.
"""

class Solution:
    # Using Two pointer reach and next reach from index i
    # reach : jump reach from index i -> arr[i]
    # nxt_reach : jump reach from index + 1 --> arr[i+1]
    def jump(self, arr):

        n, no_of_jump, reach, nxt_reach = len(arr), 0, 0, 0

        for i, j in enumerate(arr):

            if reach >= n-1:
                break

            if reach < i:
                reach = nxt_reach
                no_of_jump += 1
                if reach < i:
                    return -1
            nxt_reach = max(nxt_reach, i+j)
        return no_of_jump

    # Using Dynamic Programming
    def minJump(self, arr):
        import sys
        n = len(arr)
        jumps = [0 for _ in range(n)]
        if n == 0:
            return 0
        if n > 1 and arr[0] == 0:
            return -1
        jumps[0] = 0
        for i in range(1,n):
            mx = sys.maxsize
            jumps[i] = mx
            for j in range(i):
                if i <= j + arr[j] and jumps[j] != mx:
                    jumps[i] = min(jumps[i], jumps[j]+1)
                    break
        return jumps[n-1]




s = Solution()
arr = [2]
print(s.minJump(arr))
