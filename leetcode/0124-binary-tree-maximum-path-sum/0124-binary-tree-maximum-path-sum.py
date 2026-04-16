# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxx = [float("-inf")]
        def solve(root):
            if not root:
                return 0
            
            left = max(0,solve(root.left))
            right = max(0,solve(root.right))

            maxx[0] = max(maxx[0], left + right + root.val)
            return root.val + max(left,right)
            
        solve(root)
        return maxx[0]