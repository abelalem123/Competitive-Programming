class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph=defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i==j:
                    continue
                if  isConnected[i][j]:
                    graph[i].append(j)
        visited=set()
        
        def dfs(i):
            visited.add(i)
            for child in graph[i]:
                if child not in visited:
                    dfs(child)
                    visited.add(child)
        print(graph)
        count=0
        for i in range(len(isConnected)):
            if i not in visited:
                count+=1
                dfs(i)
        return count