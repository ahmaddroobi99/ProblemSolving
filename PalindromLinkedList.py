def isPalindrome(self, head: Optional[ListNode]) -> bool:
	res = ""

	while head:
		res += str(head.val)
		head = head.next

	return res == res[::-1]


def isPalindrome(self, head: Optional[ListNode]) -> bool:
    stack = [];
    left, right = head, head

    while right:
        stack.append(right.val)
        right = right.next
        # move to the end of the linked list

    while left:
        if left.val == stack.pop():
            left = left.next
        else:
            return False

    return True