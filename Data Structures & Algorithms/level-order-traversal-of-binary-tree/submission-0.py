# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=collections.deque([root])
        res=[]
        while queue:
            level=[]
            length=len(queue)
            while length>0:
                node=queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                length-=1
            if level:
                res.append(level)
        return res







        