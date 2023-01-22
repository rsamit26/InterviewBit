"""
Given an array of integers, every element appears thrice except for one which occurs once.

Find that element which does not appear thrice.

Note: Your algorithm should have a linear runtime complexity.

Could you implement it without using extra memory?

Example :

Input : [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
Output : 4

"""

class Solution:

    def find_one_3(self, arr):
        n = len(arr)
        A = list(A)
        if n == 1:
            return A[0]
        A = sorted(A)
        i = 0
        while(i < len(A)-2):
            if A[i] == A[i+1]:
                i = i + 3
            else: 
                return A[i]
        return A[-1]       

        
