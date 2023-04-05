# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        ans = []
        self.buildPath(root,"", ans)
        return ans

    def buildPath(self,node, path, ans):
        if not node.left and not node.right:
            ans.append(path + str(node.val))
        if node.left:
            self.buildPath(node.left, path + str(node.val) + "->", ans)
        if node.right:
            self.buildPath(node.right, path + str(node.val) + "->", ans)
        