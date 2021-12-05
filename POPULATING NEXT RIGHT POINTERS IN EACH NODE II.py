"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = deque()
        queue.append(root)

        while queue:
            curr = None
            nxt = None

            for _ in range(len(queue)):
                if not curr:
                    curr = queue.popleft()
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)


                elif not nxt:
                    nxt = queue.popleft()
                    curr.next = nxt
                    if nxt.left:
                        queue.append(nxt.left)
                    if nxt.right:
                        queue.append(nxt.right)

                else:
                    curr = queue.popleft()
                    nxt.next = curr
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                    nxt = curr

        return root

