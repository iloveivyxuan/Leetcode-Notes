# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None: return None

        result = ListNode()
        curr = result
        while l1 and l2:
            if l1.val < l2.val:
                curr.val = l1.val
                l1 = l1.next
            else:
                curr.val = l2.val
                l2 = l2.next
            curr.next = ListNode()
            curr = curr.next

        curr.val = l1.val if l1 else l2.val
        curr.next = l1.next if l1 else l2.next

        return result
