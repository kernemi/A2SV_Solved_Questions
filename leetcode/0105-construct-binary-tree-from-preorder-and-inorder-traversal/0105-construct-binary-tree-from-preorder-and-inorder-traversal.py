# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        dicts = {inorder[i]:i for i in range(len(inorder))}
        self.idx = 0

        def build(left,right):
            if left > right:
                return None

            root = TreeNode(preorder[self.idx])
            self.idx += 1
            index = dicts[root.val]

            root.left = build(left,index - 1)
            root.right = build(index + 1, right)
            
            return root
        
        return build(0,len(inorder)-1)

        
        