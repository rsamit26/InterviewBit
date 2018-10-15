# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution3:
#     # @param a list of ListNode
#     # @return a ListNode
#     def mergeKLists(self, lists):
#         import heapq
#
#         dummy = ListNode(0)
#         current = dummy
#
#         heap = []
#         for sorted_list in lists:
#             if sorted_list:
#                 heapq.heappush(heap, (sorted_list.val, sorted_list))
#
#         while heap:
#             smallest = heapq.heappop(heap)[1]
#             current.next = smallest
#             current = current.next
#             if smallest.next:
#                 heapq.heappush(heap, (smallest.next.val, smallest.next))
#
#         return dummy.next

