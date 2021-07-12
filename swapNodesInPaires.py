# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)

        dummy.next = head

        start = dummy

        while dummy.next and dummy.next.next:
            temp1 = dummy.next  # A
            temp2 = temp1.next  # B

            dummy.next, temp2.next, temp1.next = temp2, temp1, temp2.next

            dummy = temp1

        return start.next
