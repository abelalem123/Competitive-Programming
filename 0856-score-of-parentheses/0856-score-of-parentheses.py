class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        cur = 0
        for c in s:
            if c == '(':
                stack.append(cur)
                cur = 0
            else:
                cur = stack.pop() + max(1, cur*2)
        return cur 
        # return eval(s.replace(")(",")+(").replace("()","1").replace(")",")*2"))