class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(list)
        
        for i in range(len(equations)):
            a=equations[i][0]
            b=equations[i][1]
            graph[a].append([values[i],b])
            graph[b].append([(1/values[i]),a])
        ans=[]
        print(graph)
        def bfs(a,b):
            count=1
            visited=set()
            print(a,b,visited)
            q=deque()
            q.append([1,a])
            if a not in graph or b not in graph:
                print('hey')
                return -1
            while q:
                m,node=q.popleft()
                count=m
                print(m,node)
                if node==b:
                    return count
                for child in graph[node]:
                    print(child,visited)
                    if child[1] not in visited:
                        q.append([child[0]*m,child[1]])
                        visited.add(child[1])
            return -1
        for i in queries:
            x=bfs(i[0],i[1])
            ans.append(x)
        return ans
       