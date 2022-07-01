from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list1 = ListNode(1,ListNode(2, ListNode(3)))
list2 = ListNode(2,ListNode(3, ListNode(4)))


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        sorted_list_node = ListNode()
        sorted_list = list()
        # if not list1 and not list2:
        #     empt = ListNode()
        #     empt.next = None
        #     empt = empt.next
        #     return empt
        if list1:
            while True:
                sorted_list.append(list1.val)
                list1 = list1.next
                if not list1:
                    break
        if list2:
            while True:
                sorted_list.append(list2.val)
                list2 = list2.next
                if not list2:
                    break
        sorted_list = sorted(sorted_list)
        prev_item = None
        for item in sorted_list:
            if not prev_item:
                prev_item = ListNode(item)
                sorted_list_node = prev_item
            else:
                prev_item.next = ListNode(item)
                prev_item = prev_item.next

        return sorted_list_node


s = Solution()
z = s.mergeTwoLists(list1, list2)
print(z)
for i in range(6):
    if z:
        print(z.val)
        z = z.next
