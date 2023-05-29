class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set([0])
        def bfs(node):
            queue=deque([node])
            while queue:
                node=queue.popleft()
                for neighbour in rooms[node]:
                    if neighbour not in visited and neighbour != node and node in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
        
        for i in range(len(rooms)):
            bfs(i)
        print(visited)
        return len(visited)==len(rooms)