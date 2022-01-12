# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dumy = ListNode()
        tail = dumy

        while l1 and l2:
            if l1.val > l2.val:
                tail.next = l2
                l2 = l2.next

            else:
                tail.next = l1
                l1 = l1.next

            tail = tail.next

        if l1:
            tail.next = l1

        if l2:
            tail.next = l2

        return dumy.next

