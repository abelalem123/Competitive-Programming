class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans=[]
        graph=defaultdict(list)
        q=deque()
        incoming=[0 for i in range(numCourses)]
        for i in prerequisites:
            graph[i[1]].append(i[0])
            incoming[i[0]]+=1
        visited=set()
        ans=[]
        
        for c in range(numCourses):
            if incoming[c]==0:
                q.append(c)
        while q:
            c=q.popleft()
            ans.append(c)
            for child in graph[c]:
                incoming[child]-=1
                if incoming[child]==0:
                    q.append(child)
        if len(ans)!=numCourses:
            return []
        return ans
        
       