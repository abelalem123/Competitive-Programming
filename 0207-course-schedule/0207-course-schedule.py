class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ans=[]
        graph=defaultdict(list)
        incoming=[0 for i in range(numCourses)]
        
        for course,pre in prerequisites:
            graph[pre].append(course)
            incoming[course]+=1
        q=deque()
        
        for num in range(numCourses):
            if incoming[num]==0:
                q.append(num)
        while q:
            c=q.popleft()
            ans.append(c)
            for child in graph[c]:
                incoming[child]-=1
                if incoming[child]==0:
                    q.append(child)
        if len(ans)!=numCourses:
            return False
        return True