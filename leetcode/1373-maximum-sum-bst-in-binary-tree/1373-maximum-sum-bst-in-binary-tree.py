# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        answer = [0]

        def solve(root):
            if not root:
                return (True, float("inf"), float("-inf"), 0)

            leftBST,minl, maxl, suml = solve(root.left)
            rightBST, minr, maxr, sumr = solve(root.right)

            if leftBST and rightBST and maxl < root.val < minr:
                total = root.val + suml + sumr
                answer[0] = max(answer[0], total)

                return (True, min(root.val,minl), max(root.val, maxr), total)
            else:
                return (False, 0, 0, 0)

        solve(root)
        return answer[0]