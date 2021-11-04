class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        slow.next = self.reverseList(slow.next)
        head_1 = head
        head_2 = slow.next
        slow.next = None

        while head_1 and head_2:
            temp1 = head_1.next
            temp2 = head_2.next
            head_1.next = head_2
            head_1 = temp1
            head_2.next = head_1
            head_2 = temp2

    def reverseList(self, head):
        if not head or not head.next:
            return head
        reversed_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reversed_head