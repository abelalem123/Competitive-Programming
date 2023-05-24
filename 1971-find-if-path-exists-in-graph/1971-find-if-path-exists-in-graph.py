class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges:
            return True
        def bfs(node,graph,dest):
            visited=set([node])
            queue=deque([node])
            while queue:
                
                node=queue.popleft()
                print(node)
                if node==dest:
                    return True

                for neighbour in graph[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour) 
            return False
        graph=defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        for i in range(len(edges)):
            if i==source:
                return bfs(i,graph,destination)