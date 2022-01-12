# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        arr = []
        while (head):
            arr.append(head.val)
            head = head.next

        def convertToTree(left, right):
            if (left > right):
                return None
            mid = left + (right - left) // 2
            root = TreeNode(arr[mid])
            root.left = convertToTree(left, mid - 1)
            root.right = convertToTree(mid + 1, right)
            return root

        return convertToTree(0, len(arr) - 1)