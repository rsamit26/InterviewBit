"""
A hotel manager has to process N advance bookings of rooms for the next season. His hotel has K rooms.
Bookings contain an arrival date and a departure date. He wants to find out whether there are enough
rooms in the hotel to satisfy the demand. Write a program that solves this problem in time O(N log N) .

Input:

First list for arrival time of booking.
Second list for departure time of booking.
Third is K which denotes count of rooms.

Output:

A boolean which tells whether its possible to make a booking.
Return 0/1 for C programs.
O -> No there are not enough rooms for N booking.
1 -> Yes there are enough rooms for N booking.
Example :

Input :
        Arrivals :   [1 3 5]
        Departures : [2 6 8]
        K : 1

Return : False / 0

At day = 5, there are 2 guests in the hotel. But I have only one room.
"""

class Solution:
    def hotel(self, arrive, depart, K):
        events = [(t, 1) for t in arrive] + [(t, 0) for t in depart]


        events = sorted(events)
        print(events)

        guests = 0

        for event in events:
            if event[1] == 1:
                guests += 1
            else:
                guests -= 1

            if guests > K:
                return 0

        return 1



"""Testing code """

s = Solution()
a = [13, 14, 36, 19, 44, 1, 45, 4, 48, 23, 32, 16, 37, 44, 47, 28, 8, 47, 4, 31, 25, 48, 49, 12, 7, 8]
d = [28, 27, 61, 34, 73, 18, 50, 5, 86, 28, 34, 32, 75, 45, 68, 65, 35, 91, 13, 76, 60, 90, 67, 22, 51, 53]

print(s.hotel(a, d, 23))
