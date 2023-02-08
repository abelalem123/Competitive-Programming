class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill)==2:
            return skill[0]*skill[1]
        skill.sort()
        teams=[]
        l=0
        r=len(skill)-1
        while l<r:
            teams.append([skill[l],skill[r]])
            l+=1
            r-=1
        sumx=teams[0][0]*teams[0][1]
        for i in range(1,len(teams)):
            if teams[i-1][0]+teams[i-1][1]!=teams[i][0]+teams[i][1]:
                return -1
            sumx+=teams[i][0]*teams[i][1]
        return sumx