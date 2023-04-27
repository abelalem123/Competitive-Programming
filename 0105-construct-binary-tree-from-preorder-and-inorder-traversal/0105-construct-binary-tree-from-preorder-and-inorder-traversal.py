# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        rootVal=preorder.pop(0)
        root=TreeNode(rootVal)
        rootidx=inorder.index(rootVal)
        
        root.left=self.buildTree(preorder,inorder[:rootidx])
        root.right=self.buildTree(preorder,inorder[rootidx+1:])
        
        return root