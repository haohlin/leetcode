import heapq
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = []
        sentinal = ListNode()
        temp = sentinal
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(q, (lists[i].val, i))
                lists[i] = lists[i].next
        while q:
            min_val, min_i = heapq.heappop(q)
            temp.next = ListNode(min_val)
            temp = temp.next
            if lists[min_i]:
                next_val = lists[min_i].val
                lists[min_i] = lists[min_i].next
                heapq.heappush(q, (next_val, min_i))
        return sentinal.next
