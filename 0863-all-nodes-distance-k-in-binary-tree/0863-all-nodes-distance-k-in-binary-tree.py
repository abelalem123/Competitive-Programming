# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph=defaultdict(list)
        
        def dfs(root):
            if not root:
                return
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                dfs(root.left)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                dfs(root.right)
        dfs(root)
        print(graph)
        if k>len(graph):
            return []
        q=deque()
        visited=set()
        visited.add(target.val)
        count=0
        q.append(target.val)
       
        while q:
            if count==k:
                print(q)
                return list(q)
                    
            for i in range(len(q)):
                node=q.popleft()
               
                for child in graph[node]:
                    if child not in visited:
                        q.append(child)
                        visited.add(child)
            count+=1
                    
        return []
        
            