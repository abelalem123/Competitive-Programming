class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # build graph
        graph = defaultdict(dict)
        for edge, prob in zip(edges, succProb):
            u, v = edge
            graph[u][v] = prob
            graph[v][u] = prob
            
        heap = []
       
        heapq.heappush(heap, (-1, start_node))
        
      
        visited = set()
        while heap:
            prob, node = heapq.heappop(heap)
            if node == end_node:
                # revert to positive when return
                return  - prob
            if node in visited:
                continue
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    edgeProb = graph[node][nei]
                    heapq.heappush(heap, (prob * edgeProb, nei))
                    
        return 0.0