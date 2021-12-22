# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _findMid(self, head):
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return prev, slow

    def _revList(self, endOfL2):
        prev, cur = None, endOfL2
        while cur:
            nextCur = cur.next
            cur.next = prev
            prev, cur = cur, nextCur
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return None
        if not head.next: return head

        endOfL1, endOfL2 = self._findMid(head)
        endOfL1.next = None
        l1 = head
        l2 = self._revList(endOfL2)

        dummy = tail = ListNode()
        isL1 = True

        while l1 and l2:
            if isL1:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            isL1 = not isL1
            tail = tail.next
        if l1: tail.next = l1
        if l2: tail.next = l2

        return dummy.next
