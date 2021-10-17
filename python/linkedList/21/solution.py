# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1 = l1.next
        prev = head
        while l1 or l2:
            if l1 and l2:
                if l1.val > l2.val:
                    prev.next = l2
                    prev = l2
                    l2 = l2.next
                else: 
                    prev.next = l1
                    prev = l1
                    l1 = l1.next
            elif l1 and not l2:
                prev.next = l1
                return head
            elif not l1 and l2:
                prev.next = l2
                return head
        return head