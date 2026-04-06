# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None :
            return ""
        queue = collections.deque()
        queue.append(root)
        list= []
        
        while queue:
            node = queue.popleft()
            if node:
                list.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                list.append("#")
        
        return ",".join(list)
        

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        nums = data.split(",")
        root = TreeNode(int(nums[0]))
        queue = collections.deque([root])
        i=1  
        while queue and i < len(nums):
            parent = queue.popleft()
            if nums[i] != "#":
                leftSon = TreeNode(int(nums[i]))
                parent.left = leftSon
                queue.append(leftSon)
            i += 1  
            if i < len(nums):
                if nums[i] != "#":
                    rightSon = TreeNode(int(nums[i]))
                    parent.right = rightSon
                    queue.append(rightSon)
                i += 1
        return root
