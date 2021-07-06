class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = ListNode(0, None)
        curr = temp = node
        carry = 0
        while l1 or l2 or carry != 0:
            sum1 = 0
            if l1:
                sum1 += l1.val
                l1 = l1.next
            if l2:
                sum1 += l2.val
                l2 = l2.next
            sum1 += carry
            carry = sum1//10
            sum1 = sum1 % 10
            node = ListNode(sum1, None)
            temp.next = node
            temp = node
        return curr.next
