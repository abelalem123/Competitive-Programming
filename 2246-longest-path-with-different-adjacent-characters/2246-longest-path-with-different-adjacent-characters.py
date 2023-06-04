class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph=defaultdict(list)
        for i,c in enumerate(parent):
            graph[c].append(i)
        m=1
        def dfs(root):
            nonlocal m
            longest=sLongest=0
            for child in graph[root]:
                path=dfs(child)
                if s[child]!=s[root]:
                    if path>longest:
                        sLongest=longest
                        longest=path
                    elif path>sLongest:
                        sLongest=path
                m=max(m,longest+sLongest+1)
            return longest+1
        dfs(0)
        return m
                
        