def kthSmallest(self, root: TreeNode, k: int) -> int:
    # inorder traversal, track smallest reduce k until 0 return val

    while root:

        cur = root.left

        while cur and cur.right and cur.right != root:
            cur = cur.right

        if cur == None or cur.right == root:
            k -= 1
            if k == 0:
                return root.val
            root = root.right

        else:
            cur.right = root
            root = root.left