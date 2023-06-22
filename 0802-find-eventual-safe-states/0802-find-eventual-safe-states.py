class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        incoming=[0 for i in range(len(graph))]
        gr=defaultdict(list)
        ans=[]
        for i in range(len(graph)):
            for j in graph[i]:
                gr[j].append(i)
                incoming[i]+=1
        q=deque()
        for i in range(len(graph)):
            if incoming[i]==0:
                q.append(i)
        while q:
            c=q.popleft()
            ans.append(c)
            for child in gr[c]:
                incoming[child]-=1
                if incoming[child]==0:
                    q.append(child)
        return sorted(ans)