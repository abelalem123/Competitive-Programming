class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(position[i],speed[i]) for i in range(len(position))]
        arr.sort(reverse=True)
        stk = []
        ans = 0
        for pos,spd in arr:
            curr = (target-pos)/spd
           
            if len(stk)==0 or curr > stk[-1]:
                stk.append(curr)
                ans+=1
        return ans