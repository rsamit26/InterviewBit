"""
As it is Tushar’s Birthday on March 1st, he decided to throw a party to all his
friends at TGI Fridays in Pune.
Given are the eating capacity of each friend, filling capacity of each dish and
cost of each dish. A friend is satisfied if the sum of the filling capacity of
dishes he ate is equal to his capacity. Find the minimum cost such that all of
Tushar’s friends are satisfied (reached their eating capacity).

NOTE:

Each dish is supposed to be eaten by only one person. Sharing is not allowed.
Each friend can take any dish unlimited number of times.
There always exists a dish with filling capacity 1 so that a solution always exists.
Input Format

Friends : List of integers denoting eating capacity of friends separated by space.
Capacity: List of integers denoting filling capacity of each type of dish.
Cost :    List of integers denoting cost of each type of dish.
Constraints:
1 <= Capacity of friend <= 1000
1 <= No. of friends <= 1000
1 <= No. of dishes <= 1000

Example:

Input:
    2 4 6
    2 1 3
    2 5 3

Output:
    14

Explanation:
    First friend will take 1st and 2nd dish, second friend will take 2nd dish
    twice.  Thus, total cost = (5+3)+(3*2)= 14
"""

class Solution:

    def tushar_birthday(self, friends, dishes, price):
        max_capacity = max(friends) # maxium capacity of a friend
        # Memo table for storing price for capacity [0.......max_capacity]
        lookup = [None for _ in range(max_capacity+1)]
        lookup[0] = 0 # Base Case for Nil capacity price is 0

        for i in range(max_capacity):
            for j in range(len(dishes)):
                temp_cap = i + dishes[j]
                if temp_cap <= max_capacity:
                    if lookup[temp_cap] is None or lookup[temp_cap] > lookup[i] + price[j]:
                        lookup[temp_cap] = lookup[i] + price[j]
        s = 0
        for i in range(len(friends)):
            s+= lookup[friends[i]]
        return s

s = Solution()
f = [4,6]
d = [1,3]
p = [5,3]
print(s.tushar_birthday(f,d,p))
