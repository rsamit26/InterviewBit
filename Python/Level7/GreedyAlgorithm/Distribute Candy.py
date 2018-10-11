"""
There are N children standing in a line. Each child is assigned a rating value.

 You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Sample Input :

Ratings : [1 2]
Sample Output :

3
The candidate with 1 rating gets 1 candy and candidate with rating cannot get 1 candy as 1 is its neighbor.
So rating 2 candidate gets 2 candies. In total, 2+1 = 3 candies need to be given out.
"""


class Solution:

    def candies(self, arr):
        n = len(arr)
        if n == 1:
            return 1
        candies = [1] * n
        for i in range(n):
            if i == 0:  # corner case left and right side
                if arr[i] > arr[i + 1]:
                    candies[i] = candies[i + 1] + 1

            elif i == n - 1:
                if arr[i] > arr[i - 1]:
                    candies[i] = candies[i - 1] + 1

            else:
                if arr[i] > arr[i + 1] and arr[i] > arr[i - 1]:
                    candies[i] = max(candies[i - 1], candies[i + 1]) + 1
                elif arr[i] > arr[i + 1]:
                    candies[i] = candies[i + 1] + 1
                elif arr[i] > arr[i - 1]:
                    candies[i] = candies[i - 1] + 1

        for i in range(n - 1, -1, -1):
            if i == 0:  # corner case left and right side
                if arr[i] > arr[i + 1]:
                    candies[i] = candies[i + 1] + 1

            elif i == n - 1:
                if arr[i] > arr[i - 1]:
                    candies[i] = candies[i - 1] + 1

            else:
                if arr[i] > arr[i + 1] and arr[i] > arr[i - 1]:
                    candies[i] = max(candies[i - 1], candies[i + 1]) + 1
                elif arr[i] > arr[i + 1]:
                    candies[i] = candies[i + 1] + 1
                elif arr[i] > arr[i - 1]:
                    candies[i] = candies[i - 1] + 1

        return sum(candies)

    def method02(self, arr):
        n = len(arr)

        candies = [1] * n

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1

        return sum(candies)


s = Solution()
arr = [1,2,1,5]
print(s.candies(arr))
print(s.method02(arr))
