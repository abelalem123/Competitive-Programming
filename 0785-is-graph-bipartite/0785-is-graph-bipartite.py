class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color={}
        def dfs(node):
            for neighbour in graph[node]:
                if neighbour in color:
                    if color[neighbour]==color[node]:
                        return False
                else:
                    color[neighbour]=1-color[node]
                    if not dfs(neighbour):
                        return False
            return True
        for node in range(len(graph)):
            if node not in color:
                color[node] = 0
                if not dfs(node):
                    return False

        return True

        