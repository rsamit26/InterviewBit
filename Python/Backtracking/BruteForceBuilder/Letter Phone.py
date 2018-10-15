"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



The digit 0 maps to 0 itself.
The digit 1 maps to 1 itself.

Input: Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Make sure the returned strings are lexicographically sorted.
"""


class Solution:

    # def phone_helper(self, arr, n, curr, res):
    #
    #     if

    def phone_comb(self, digits):
        data = {'0': ["0"], '1': ["1"], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}
        n = len(digits)
        res = []  # Storing the combination of given digits

        for i in range(n):
            if not res:
                res = data[digits[i]]  # Initialising the result with the first digit corresponding letter
            else:
                curr = []
                # populating the result with map data
                for j in res:  # res = [x,y,z] ; j = x
                    for k in data[digits[i]]:  # data[s[i]] = [a,b,c] ; k = a , k = b, k = c
                        curr.append(j + k)  # curr = [xa, xb, xc]
                res = curr
        return res


class Solution2:
    def phone_comb(self, digits):
        data = {'0': ["0"], '1': ["1"], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}

        n, result = len(digits), []

        if not digits:
            return []
        self.phone_helper(result, digits, data, "", 0)

        return result

    def phone_helper(self, result, digits, data, curr, start):
        """ Base Case :: when length of combination is equal to length of given digits

                        i.e. curr = [adj] , start= 3, len(digits) = 3 then append curr in result
          """
        if start == len(digits):
            result.append(curr)
            return
        else:
            for i in data[digits[start]]:
                self.phone_helper(result, digits, data, curr + i, start + 1)


""" Testing Solutions """

s1 = Solution()
print(s1.phone_comb("234"))

s = Solution2()
print(s.phone_comb("234"))
