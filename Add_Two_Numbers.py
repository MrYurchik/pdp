# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        numb1 = str()
        numb2 = str()
        while l1:
            numb1 += str(l1.val)
            l1 = l1.next
        numb1 = numb1[::-1]
        while l2:
            numb2 += str(l2.val)
            l2 = l2.next
        numb2 = numb2[::-1]
        summ = str(int(numb1) + int(numb2))[::-1]
        list_node_sum = ListNode()
        prev_item = None
        for item in summ:
            if not prev_item:
                prev_item = ListNode(int(item))
                list_node_sum = prev_item
            else:
                prev_item.next = ListNode(int(item))
                prev_item = prev_item.next

        return list_node_sum





s = Solution()
suma = s.addTwoNumbers(ListNode(2,ListNode(4,ListNode(3,))), ListNode(5,ListNode(6,ListNode(4,))))

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

while suma:
    print(suma.val)
    suma = suma.next
