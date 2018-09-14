"""
Add One To Number
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plus_one(self, a):
        t = list(map(str, a))
        p = ''.join(t)
        num = int(p) + 1
        num = str(num)
        temp = []
        for i in range(len(num)):
            temp.append(int(num[i]))

        return temp


"""
Testing Code for this problem
"""

s = Solution()
a = [1, 2, 3, 4]
print(s.plus_one(a))

# output == [1,2,3,5]
