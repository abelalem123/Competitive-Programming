class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph=defaultdict(list)
        for i in range(len(routes)):
            for j in routes[i]:
                graph[j].append(i)
        q=deque()
        visited=set()
        q.append([source,0])
        while q:
            node,count =q.popleft()
            visited.add(node)
            if node==target:
                return count
            for i in graph[node]:
                for child in routes[i]:
                    if child not in visited:
                        q.append([child,count+1])
                        visited.add(child)
                routes[i]=[]
        return -1