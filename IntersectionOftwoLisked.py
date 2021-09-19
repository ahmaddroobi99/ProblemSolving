# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA, curB = headA, headB
        a, b = 0, 0
        while curA:
            a += 1
            curA = curA.next

        while curB:
            b += 1
            curB = curB.next

        if a > b:
            curL = headA
            diff = a - b
            curS = headB


        else:
            curL = headB
            diff = b - a
            curS = headA
        i = 0
        while i < diff:
            i += 1
            curL = curL.next

        while curL != curS:
            curL = curL.next
            curS = curS.next

        return curL








