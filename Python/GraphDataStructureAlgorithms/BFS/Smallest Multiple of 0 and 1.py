"""
You are given an integer N. You have to find smallest multiple of N which
consists of digits 0 and 1 only. Since this multiple could be large, return it
in form of a string.

Note:

Returned string should not contain leading zeroes.
For example,

For N = 55, 110 is smallest multiple consisting of digits 0 and 1.
For N = 2, 10 is the answer.
"""

class Solution:

    # Using BFS
    def solve(self, n):
        queue, visited = [], []
        s = "1"
        queue.append(s)
        while queue:
            u = queue.pop(0)
            rem = int(u)%n
            if rem == 0:
                return u
            elif rem not in visited:
                visited.append(rem)
                queue.append(u + "0")
                queue.append(u + "1")



    def multiple(self, n):
        if self.check_0_1(n):
            return str(n)
        i = 1
        while True:
            if self.check_0_1(n*i):
                return str(n*i)
            i+= 1
        return False


    def check_0_1(self, n):
        n = str(n)
        for i in n:
            if int(i) != 0 and int(i) != 1:
                return False
        return True

    def method_02(self, n):
        status = False
        i = 1
        while status != True:

            mul = n*i
            s = set('01')
            mul = str(mul)
            if set(mul).issubset(s):
                flag = True
                break
            else:
                i+=1
        return mul
s = Solution()
# print(s.method_02(1070))
# print(s.multiple(1070))
print(s.solve(1070))
