# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        sentinel = ListNode(0, head)
        cur = sentinel
        cur_loc = 0

        while cur and cur_loc + 1 != left:
            cur = cur.next
            cur_loc += 1
        pre_left_node = cur
        
        while cur and cur_loc != right:
            cur = cur.next
            cur_loc += 1
        right_node = cur
        
        pre_left_node.next = self.reverse(pre_left_node.next, right_node.next)
        return sentinel.next
        

    def reverse(self, head, end):
        if head is end or head.next is end:
            return head

        next_head = self.reverse(head.next, end)
        head.next.next = head
        head.next = end

        return next_head