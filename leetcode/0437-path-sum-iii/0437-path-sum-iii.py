# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        def check(root,summ):
            if not root:
                return 0
                
            count = 0
            summ += root.val
            if summ == targetSum:
                count += 1
            return count + check(root.left,summ) + check(root.right,summ)
        
        return check(root, 0) + self.pathSum(root.left,targetSum) + self.pathSum(root.right,targetSum)