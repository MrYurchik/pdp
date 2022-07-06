# Definition for singly-linked list.
from typing import Optional
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            if cur.val == val:
                if not prev:
                    head = cur.next
                else:
                    prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return head

# head = [1,2,6,3,4,5,6]



val = 6
s = Solution()
s.removeElements(head, val)
print(type(head))
while head:
    print(head.val)
    head = head.next
