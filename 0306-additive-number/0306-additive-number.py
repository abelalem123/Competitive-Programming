class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(first,second,idx):
            if idx>=len(num):
                return True
            for k in range(idx,len(num)):
                curr=num[idx:k+1]
                if idx!=k and curr[0]=='0':
                    return False
                if int(first)+int(second)==int(curr) and dfs(second,curr,k+1):
                    return True
        for i in range(len(num)-2):
            first=num[:i+1]
            if i!=0 and first[0]=='0':
                break
            for j in range(i+1,len(num)-1):
                second=num[i+1:j+1]
                if i+1!=j and second[0]=='0':
                    break
                if dfs(first,second,j+1):
                    return True
        return False
    
             
            