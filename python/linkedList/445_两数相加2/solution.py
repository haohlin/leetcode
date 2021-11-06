# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        result = self.sumList(l1, l2)
        return self.reverse(result)

    def reverse(self, head):
        if not head or not head.next:
            return head
        reversed_head = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return reversed_head

    def sumList(self, l1, l2):
        carry = 0
        head = ListNode()
        cur_node = head
        while l1 and l2:
            cur_sum = l1.val + l2.val + carry
            cur_node.val = cur_sum % 10
            carry = cur_sum // 10
            l1 = l1.next
            l2 = l2.next
            if l1 or l2 or carry != 0:
                new_node = ListNode()
                cur_node.next = new_node
                cur_node = cur_node.next
        while l1:
            cur_sum = l1.val + carry
            cur_node.val = cur_sum % 10
            carry = cur_sum // 10
            l1 = l1.next
            if l1 or carry != 0:
                new_node = ListNode()
                cur_node.next = new_node
                cur_node = cur_node.next
        while l2:
            cur_sum = l2.val + carry
            cur_node.val = cur_sum % 10
            carry = cur_sum // 10
            l2 = l2.next
            if l2 or carry != 0:
                new_node = ListNode()
                cur_node.next = new_node
                cur_node = cur_node.next

        if carry != 0:
            cur_node.val = carry
        return head