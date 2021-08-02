# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def search(self, head, root):
        if not head:
            return True
        if not root or root.val != head.val:
            return False
        return self.search(head.next, root.left) or self.search(head.next, root.right)

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not head:
            return True
        if not root:
            return False
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.val == head.val:
                status = self.search(head, curr)
                if status:
                    return True
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        return False
