class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        for i in edges:
            x,y =i
            graph[x].append(y)
            graph[y].append(x)
        ans=0
        for k,v in graph.items():
            if len(v)==len(graph)-1:
                ans=k
                break
        return ans
