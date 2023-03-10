class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for num in tokens:
            if num=="*":
                op1=stack.pop()
                op2=stack.pop()
                print(op1,op2,num)
                stack.append(op1*op2)
            elif num=='+':
                op1=stack.pop()
                op2=stack.pop()
                print(op1,op2,num)
                stack.append(op1+op2)
            elif num=="-":
                op1=stack.pop()
                op2=stack.pop()
                print(op1,op2,num)
                stack.append(op2-op1)
            elif num=="/":
                op1=stack.pop()
                op2=stack.pop()
                print(op1,op2,num)
                div=op2/op1
                div=ceil(div) if div<0 else floor(div)
                stack.append(div)
            else:
                stack.append(int(num))
        return stack.pop()