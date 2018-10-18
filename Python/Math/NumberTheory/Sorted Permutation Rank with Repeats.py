"""
Given a string, find the rank of the string amongst its permutations sorted
lexicographically.
Note that the characters might be repeated. If the characters are repeated,
we need to look at the rank in unique permutations.
Look at the example for more details.

Example :

Input : 'aba'
Output : 2

The order permutations with letters 'a', 'a', and 'b' :
aab
aba
baa
The answer might not fit in an integer, so return your answer % 1000003
"""

class Solution:

    # Return the rank of given string from sorted permutation of that string
    def rankPermutation(self, string):
        from collections import defaultdict
        lookup = defaultdict(int)
        for i in string:
            if lookup[string[i]] is None:
                lookup[string] = 1
            else:
                lookup[string[i]] += 1
        n, rank, i = len(string), 1, 0
        total_permutaion = self.fact(n)  # Total number of permutation
        while i < n:
            total_permutaion = total_permutaion//(n-i)
            count = self.smallComb(string, i, n-1)
            rank = rank + count*total_permutaion
            i+= 1
        return rank % 1000003
    # Counts the number of small element from string[start] in right
    def smallComb(self, string, start, end):
        count, i = 0, start+1
        while i <= end:
            if string[i] < string[start]:
                count += 1
            i+=1
        return count
    # Counts factorial of a number k
    def fact(self, k):
        f, i = 1, 1
        while i <k+1:
            f *= i
            i+=1
        return f
