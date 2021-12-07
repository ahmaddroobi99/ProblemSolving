# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def getDecimalValue(self, head: ListNode) -> int:
#         value= 0
#         while head  :
#             value += head.val+ 2*value
#             head =head.next
#         return value

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head:
            ans, head = ans * 2 + head.val, head.next
        return ans