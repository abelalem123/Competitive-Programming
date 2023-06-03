class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph=defaultdict(list)
        
        for i,c in enumerate(manager):
            if c!=-1:
                graph[c].append(i)
        print(graph)
        
        q=deque()
        visited=set()
        q.append([headID,informTime[headID]])
        visited.add(headID)
        count=0
        while q:
            for i in range(len(q)):                
                node,v=q.popleft()
                count=max(count,v)
                for child in graph[node]:
                    if child not in visited:
                        q.append([child,v+informTime[child]])
                        visited.add(child)
        
        return count
                