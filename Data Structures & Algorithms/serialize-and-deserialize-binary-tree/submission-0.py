# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        queue = collections.deque([root])
        res = []
        
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("#")
        
        return ",".join(res)
        

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = collections.deque([root])
        i = 1
        
        while queue and i < len(values):
            parent = queue.popleft()
            
            # Left child
            if values[i] != "#":
                left_child = TreeNode(int(values[i]))
                parent.left = left_child
                queue.append(left_child)
            i += 1
            
            # Right child
            if i < len(values):
                if values[i] != "#":
                    right_child = TreeNode(int(values[i]))
                    parent.right = right_child
                    queue.append(right_child)
                i += 1
        
        return root
