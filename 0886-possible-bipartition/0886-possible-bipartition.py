class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color={}
        graph=defaultdict(list)
        for i in dislikes:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
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
        
        for i in range(1,n+1):
            if i not in color:
                color[i]=0
                if not dfs(i):
                    return False
        return True