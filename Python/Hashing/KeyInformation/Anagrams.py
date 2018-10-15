"""
Given an array of strings, return all groups of strings that are anagrams. Represent a group by a list of integers
representing the index in the original list. Look at the sample case for clarification.

 Anagram : a word, phrase, or name formed by rearranging the letters of another, such as 'spar', formed from 'rasp'
 Note: All inputs will be in lower-case.
Example :

Input : cat dog god tca
Output : [[1, 4], [2, 3]]
cat and tca are anagrams which correspond to index 1 and 4.
dog and god are another set of anagrams which correspond to index 2 and 3.
The indices are 1 based ( the first element has index 1 instead of index 0).

 Ordering of the result : You should not change the relative ordering of the words / phrase
"""


class Solution:

    def anagram(self, arr):

        from collections import defaultdict
        lookup_table = defaultdict(list)

        result = []

        for i, word in enumerate(arr):
            lookup_table["".join(sorted(word))].append(i + 1)

        for k in lookup_table.values():
            result.append(k)
        return result


s = Solution()
w = ["cat", "dog", "tca", "god", "odg", "go"]

print(s.anagram(w))
