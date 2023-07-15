class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives=0
        tens=0
        for i in bills:
            if i==5:
                fives+=1
            elif i==10 and fives>=1:
                fives-=1
                tens+=1
            elif i==20 and fives>=1 and tens>=1:
                tens-=1
                fives-=1
            elif i==20 and fives>=3:
                fives-=3
            else:
                return False
        return True
                