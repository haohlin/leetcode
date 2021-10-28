from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = self.mergeSort(head)
        return res

    def mergeSort(self, head):
        if not head or not head.next:
            return head
        head_left, head_right = self.cutMid(head)
        left = self.mergeSort(head_left)
        right = self.mergeSort(head_right)
        return self.merge(left, right)

    def cutMid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        head_left = head
        head_right = slow.next
        slow.next = None
        return head_left, head_right
    
    def merge(self, head_1, head_2):
        new_list = ListNode()
        temp = new_list
        while head_1 and head_2:
            if head_1.val <= head_2.val:
                temp.next = head_1
                head_1 = head_1.next
            else:
                temp.next = head_2
                head_2 = head_2.next
            temp = temp.next
        if head_1:
            temp.next = head_1
        if head_2:
            temp.next = head_2
        return new_list.next
                
head = ListNode(4)
node_1 = ListNode(2)
node_2 = ListNode(1)
node_3 = ListNode(3)
head.next = node_1
node_1.next = node_2
node_2.next = node_3

sol = Solution()
res = sol.sortList(head)
while res:
    print(res.val)
    res = res.next