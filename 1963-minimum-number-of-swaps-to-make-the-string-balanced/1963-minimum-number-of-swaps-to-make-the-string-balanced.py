class Solution:
    def minSwaps(self, s: str) -> int:
        stk=[]
        for i in s:
            if stk and i==']':
                stk.pop()
            elif i=='[':
                stk.append(i)

        return (len(stk)+1)//2