# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter=0
        self.depth(root)
        return self.max_diameter
    
    def depth(self,root):
            if not root:
                return -1
            left=self.depth(root.left)
            right=self.depth(root.right)
            self.max_diameter=max(self.max_diameter,(left+right)+2)
            return max(left,right)+1