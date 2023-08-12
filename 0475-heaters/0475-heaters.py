class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        radius=0
        heaters.sort()
        for i,c in enumerate(houses):
            if c>heaters[-1]:
                idx=len(heaters)-1
            else:
                idx=bisect.bisect_left(heaters,c)
            f_elemnt=heaters[idx]
            if idx==0:
                s_element=heaters[idx]
            else:
                s_element=heaters[idx-1]
            m=min(abs(f_elemnt-c),abs(s_element-c))
            radius=max(m,radius)
        return radius
    