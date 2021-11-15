from typing import Optional
import random
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        cur = self.head
        result = cur.val
        i = 0
        while cur:
            rdm_val = random.randint(0, i)
            if rdm_val == 0:
                result = cur.val
            cur = cur.next
            i += 1
        return result



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()