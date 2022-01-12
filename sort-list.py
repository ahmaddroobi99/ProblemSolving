# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        def merge_list(first, second):
            dummy_head = ListNode(0, None)
            tmp = dummy_head
            while first and second:
                if first.val > second.val:
                    tmp.next = second
                    second = second.next
                else:
                    tmp.next = first
                    first = first.next
                tmp = tmp.next
            if first: tmp.next = first
            if second: tmp.next = second
            return dummy_head.next

        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        first_half = self.sortList(head)
        second_half = self.sortList(slow)
        return merge_list(first_half, second_half)