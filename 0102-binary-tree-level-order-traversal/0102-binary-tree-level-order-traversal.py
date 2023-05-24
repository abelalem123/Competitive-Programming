# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
       def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = []
        result = []

        # If the root is not null, add it to the queue
        if root:
            queue.append(root)

        # While the queue is not empty, repeat steps 4-7
        while queue:
            # Get the size of the queue and initialize an empty list to store the nodes of the current level
            size = len(queue)
            level = []

            # Loop through the elements of the current level and add them to the list
            for i in range(size):
                node = queue.pop(0)
                level.append(node.val)

                # For each element of the current level, add its children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Add the current level list to the result list
            result.append(level)

        # Return the result list
        return result