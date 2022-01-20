# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         fast ,slow =head ,head
#         while fast and fast.next :
#             slow =slow.next
#             fast=fast.next.next
#             if slow ==fast :
#                 break
#             else :
#                 return None

#         pointer =head
#         while pointer!= fast :
#             pointer = pointer.next
#             fast=fast.next

#         return pointer
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                s = head
                while s != f:
                    s = s.next
                    f = f.next
                return s
        return None