class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        distribute=[0]*k
        n=len(cookies)
        def dfs(i,zero_count):
            if n-i<zero_count:
                return float('inf')
            if i==n:
                return max(distribute)
            answer=float('inf')
            for j in range(k):
                zero_count-=int(distribute[j]==0)
                distribute[j]+=cookies[i]
                
                answer=min(answer,dfs(i+1,zero_count))
                distribute[j]-=cookies[i]
                zero_count+=int(distribute[j]==0)
                
            return answer
        return dfs(0,k)