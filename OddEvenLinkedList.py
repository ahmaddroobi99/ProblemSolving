# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        try:
            even = odd.next
            while odd and even:
                new_odd = even.next
                new_even = new_odd.next
                new_odd.next = odd.next
                odd.next = new_odd
                odd = new_odd
                even.next = new_even
                even = new_even
            return head
        except:
            return head