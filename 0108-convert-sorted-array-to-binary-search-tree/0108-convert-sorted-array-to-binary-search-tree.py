# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    def sortedArrayToBST(self,nums):
   
        if not nums:
            return None

        # Find the middle element and make it the root of the tree.
        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        # Recursively construct the left and right subtrees using the left and right halves of the array, respectively.
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root   