class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner={}
        loser={}
        ans1=[]
        ans2=[]
        for match in matches:
            if match[0] in winner.keys():
                winner[match[0]]=winner[match[0]]+1
            else:
                winner[match[0]]=1
        
        for match in matches:
            if match[1] in loser.keys():
                loser[match[1]]=loser[match[1]]+1
            else:
                loser[match[1]]=1
        
        for key in winner.keys():
            if key in loser:
                continue
            else:
                ans1.append(key)
                
        for key,val in loser.items():
            if val==1:
                ans2.append(key)
            
            
        return [sorted(ans1),sorted(ans2)]