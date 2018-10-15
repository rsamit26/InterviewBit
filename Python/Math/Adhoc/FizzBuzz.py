"""
Given a positive integer N, print all the integers from 1 to N. But for multiples of 3 print “Fizz” instead of the
number and for the multiples of 5 print “Buzz”. Also for number which are multiple of 3 and 5, prints “FizzBuzz”.

Example

N = 5
Return: [1 2 Fizz 4 Buzz]
Note: Instead of printing the answer, you have to return it as list of strings.
"""


class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        temp = []
        for i in range(1, A + 1):
            if i % 3 == 0 and i % 15 != 0:
                temp.append("Fizz")
            elif i % 5 == 0 and i % 15 != 0:
                temp.append("Buzz")
            elif i % 15 == 0:
                temp.append("FizzBuzz")
            else:
                temp.append(str(i))

        return temp


"""Testing code"""

s = Solution()
print(s.fizzBuzz(10))

# output :: ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']
