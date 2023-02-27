class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        count=0
        l=0
        r=0
        while l<len(players) and r<len(trainers):
            if players[l]<=trainers[r]:
                l+=1
                
                count+=1
           
            r+=1
        return count