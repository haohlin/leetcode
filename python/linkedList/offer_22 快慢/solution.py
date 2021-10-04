# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        location = 1
        fast = slow = head
        while fast.next:
            if location >= k:
                slow = slow.next
            fast = fast.next
            location += 1
        return slow
