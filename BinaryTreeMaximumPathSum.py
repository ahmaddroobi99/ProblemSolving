# *A node can only appear in the sequence at most once, and the path does not need to pass through the root.
# *So if we choose to go both left and right at a certain node, that node would be the "root" node of our path
# *For each node, we consider three different cases
# *1. We stop at current node, which means we neither go left nor go right
# *2. We choose either left or right
# *3. We choose both left and right

class Solution:

def maxPathSum(self, root: TreeNode) -> int:
    ans = [float("-inf")]
    def search(node, curr_max):
        if not node:
            return 0
        left_max = search(node.left, curr_max)
        right_max = search(node.right,curr_max)

        single_max = max(0,left_max, right_max)+node.val # case1 and case 2
        double_max = max(single_max, left_max+right_max+node.val) # case 3

        ans[0] = max(ans[0], single_max, double_max)
        # remember to return the value of case 1 and case 2, since if we go up, current node can't be the "root" node
        return single_max
    search(root, 0)
    return ans[0]