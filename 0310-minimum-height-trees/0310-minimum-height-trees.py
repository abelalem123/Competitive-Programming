class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph=defaultdict(set)
        if n==1:
            return [0]
        
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        leaves=deque()
        
        for i in range(n):
            if len(graph[i])==1:
                leaves.append(i)
        
        remaining=n
        while remaining>2:
            num_leaves=len(leaves)
            remaining-=len(leaves)
            
            for _ in range(num_leaves):
                leaf=leaves.popleft()
                neighbour=graph[leaf].pop()
                graph[neighbour].remove(leaf)
                if len(graph[neighbour])==1:
                    leaves.append(neighbour)
        return list(leaves)
                