class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # stack=[]
        # ans,val=0,0
        # for i in s:
        #     if i=="(":
        #         stack.append(0)
        #     elif i==")":
        #         mul=stack.pop()
        #         if mul==0:
        #             val=1
        #         else:
        #             val=mul*2
        #         if not stack:
        #             ans+=val
        #         else:
        #             stack[-1]+=val
        #     return ans
        return eval(s.replace(")(",")+(").replace("()","1").replace(")",")*2"))