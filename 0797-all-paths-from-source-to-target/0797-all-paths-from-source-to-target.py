class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        ans=[]
        visited=set()
        def dfs(root,single):
            if root==n-1:
                ans.append(single)
            for child in graph[root]:
                print(child,visited,single)
                dfs(child,single+[child])
        dfs(0,[0])
        return ans