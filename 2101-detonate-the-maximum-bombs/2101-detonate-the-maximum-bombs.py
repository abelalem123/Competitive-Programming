class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph=defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i==j:
                    continue
                if bombs[i][2]>=math.sqrt((bombs[i][0]-bombs[j][0])**2+(bombs[i][1]-bombs[j][1])**2):
                    graph[i].append(j)
        
        def dfs(i):
            count=1
            for child in graph[i]:
                if child not in visited:
                    visited.add(child)
                    count+=dfs(child)
            return count
        
        ans=0
        for i in range(len(bombs)):
            visited=set([i])
            count=dfs(i)
            ans=max(count,ans)
        return ans