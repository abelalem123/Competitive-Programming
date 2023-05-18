"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        def dfs(node,depth):
            if not node:
                return depth
            maxd=depth
            for child in node.children:
                d=dfs(child,depth+1)
                maxd=max(maxd,d)
            return maxd
        return dfs(root,1)