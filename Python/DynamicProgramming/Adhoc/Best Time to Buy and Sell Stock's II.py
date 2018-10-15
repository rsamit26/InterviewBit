"""Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as
you like (ie, buy one and sell one share of the stock multiple times).

However, you may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).

Example :

Input : [1 2 3]
Return : 2

"""

class Solution:
    ## Greedy Approach
    def method_02(self, arr):
        profit = 0
        for i in range(len(arr)-1):
            profit += max(arr[i+1]-arr[i], 0)
        return profit
    
    #Using Recursion
    def buyAndSell(self, arr):
        profit = []
        self.helper(arr, profit)
        return sum(profit)

    def helper(self, arr, profit):
        n = len(arr)
        if n == 0:
            return
        else:
            i = 1
            while i < n:
                if arr[i-1] < arr[i]:
                    break
                i+=1
            b = i-1
            j = b +1
            while j < n:
                if arr[j-1]> arr[j]:
                    break
                j+=1
            s = j-1
            profit.append(arr[s]-arr[b])
            self.helper(arr[s+1:], profit)





s = Solution()
a = [7,1,5,3,6,4]
print(s.buyAndSell(a))
print(s.method_02(a))
