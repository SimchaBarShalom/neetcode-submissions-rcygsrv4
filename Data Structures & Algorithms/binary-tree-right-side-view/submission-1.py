# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        list = []  
        if root is None:
            return list
        queue = deque() 
        queue.append(root)
        while queue: 
            levelSize = len(queue) 
            for i in range(levelSize):
                node = queue.popleft() 
                if i == levelSize - 1:
                    list.append(node.val)
                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return list