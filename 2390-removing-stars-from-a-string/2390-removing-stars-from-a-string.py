class Solution:
    def removeStars(self, s: str) -> str:
        k, A = 0, list(s)

        for i, c in enumerate(s):
            if c == '*':
                k -= 1
            else:
                A[k] = c
                k += 1

        return ''.join(A[:k])
#         stack=[]
#         for i in range(len(s)):
#             if s[i]=='*':
#                 stack.pop()
#             else:
#                 stack.append(s[i])
            
#         return "".join(stack)
