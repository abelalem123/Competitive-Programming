class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set() for _ in range(n)]
        graph=defaultdict(list)
        incoming=defaultdict(int)
        q=deque()
        for start,end in edges:
            graph[start].append(end)
            incoming[end]+=1
        for i in range(n):
            if incoming[i]==0:
                q.append(i)
        while q:
            c=q.popleft()
     
            for child in graph[c]:
                incoming[child]-=1
                ans[child].add(c)
                ans[child].update(ans[c])
                # for i in ans[c]:
                #     if i not in ans[child]:
                #         ans[child].append(i)
                # ans[child].extend(ans[c])
               
                if incoming[child]==0:
                    q.append(child)
        ans = [(sorted(list(s))) for s in ans]
        return ans