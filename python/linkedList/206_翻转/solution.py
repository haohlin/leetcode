# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        return self.reverse(head)
    def reverse(self, head):
        if head.next == None:
            return head
        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return temp

class Solution2:
    # 迭代
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev