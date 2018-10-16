"""
How many minimum numbers from fibonacci series are required such that sum of
numbers should be equal to a given Number N?
Note : repetition of number is allowed.

Example:

N = 4
Fibonacci numbers : 1 1 2 3 5 .... so on
here 2 + 2 = 4
so minimum numbers will be 2
"""

class Solution:
    # Greedy Algo
    def minFib(self, n):
        fib = []
        self.fibSeries(fib, n)

        count, j = 0, len(fib) -1

        while n > 0:
            count += n//fib[j]
            n  %= fib[j]
            j-=1
        return count

    def fibSeries(self, fib, n):
        fib.append(0)
        fib.append(1)
        fib.append(1)
        i = 3
        while True:
            next = fib[i-1]+fib[i-2]
            if next > n:
                return
            fib.append(next)
            i+= 1




s = Solution()
print(s.minFib(17))
