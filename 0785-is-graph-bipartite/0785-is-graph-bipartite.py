class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color={}
        def dfs(node):
            for child in graph[node]:
                if child in color:
                    if color[child]==color[node]:
                        return False
                else:
                    color[child]=1-color[node]
                    if not dfs(child):
                        return False
            return True
        
        for i in range(len(graph)):
            if i not in color:
                color[i]=0
                if not dfs(i):
                    return False
        return True