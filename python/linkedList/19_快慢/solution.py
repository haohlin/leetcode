# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or not head.next:
            return None
        fast = slow = head 
        for i in range(n + 1):
            if fast == None:
                return head.next
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        if n == 1:
            slow.next = None
        else:
            slow.next = slow.next.next
        return head