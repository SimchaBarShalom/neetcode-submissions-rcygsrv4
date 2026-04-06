# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath=float('-inf')
        self.dfs(root)
        return self.maxPath

    def dfs(self, root: Optional[TreeNode]) -> int:  
        if not root:
            return 0
        left=max(self.dfs(root.left),0)
        right=max(self.dfs(root.right),0)
        self.maxPath=max(self.maxPath,root.val+left+right)
        return root.val+max(left,right)