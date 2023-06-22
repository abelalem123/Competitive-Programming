class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph=defaultdict(list)
        incoming=defaultdict(int)
        ans=[]
        for i,r in enumerate(recipes):
            for ing in ingredients[i]:
                graph[ing].append(r)
                incoming[r]+=1
        q = deque()
        for s in supplies:
            q.append(s)
        while q:
            c=q.popleft()
            if c in recipes:
                ans.append(c)
            for child in graph[c]:
                incoming[child]-=1
                if incoming[child]==0:
                    q.append(child)
        # if len(ans)!=len(recipes):
        #     return []
        return ans