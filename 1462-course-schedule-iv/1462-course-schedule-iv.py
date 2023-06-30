class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if prerequisites==[]:
            return [False]*len(queries)
        
        graph=defaultdict(list)
        incoming=defaultdict(int)
        for u,v in prerequisites:
            graph[u].append(v)
            incoming[v]+=1
        pres=[set() for i in range(numCourses)]
       
        print(pres)
        q=deque()
        ans=[]
        for i in range(numCourses):
            if incoming[i]==0:
                q.append(i)
        
        while q:
            curr=q.popleft()
            # print(curr)
            for child in graph[curr]:
                incoming[child]-=1
                
                pres[child].add(curr)
                if pres[curr]:
                    pres[child].update(pres[curr])
               
                if incoming[child]==0:
                    q.append(child)
        print(pres)
        for s,e in queries:
            ans.append(s in pres[e])
        return ans