# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root: return root
        q = [root]
        ans = []
        while q:
            t = q.copy()
            q.clear()

            r = 0
            for node in t:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                r = node.val
            ans.append(r)
        return ans