class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        
        for u,v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        
        start=adjacentPairs[0][0]
        
        for k,v in graph.items():
            if len(v)==1:
                start=k
                break
        visited=set()
        ans=[]
        
        def dfs(node):
            visited.add(node)
            # ans.append(node)
            for child in graph[node]:
                if child in visited: continue
                dfs(child)
            ans.append(node)
        dfs(start)
        return ans
    
   