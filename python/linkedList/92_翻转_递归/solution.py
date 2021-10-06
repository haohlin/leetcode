# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverseN(head, n):
            if n == 0:
                self.res = head.next
                return head
            temp = reverseN(head.next, n-1)
            head.next.next = head
            head.next = self.res
            return temp
        if right - left < 1:
            return head
        self.res = ListNode(-1)
        r_head = head
        temp_left = left
        while temp_left > 2:
            r_head = r_head.next
            temp_left -= 1
        if left == 1:
            head = reverseN(head, right - left)
        else:
            r_head.next = reverseN(r_head.next, right - left)
        return head