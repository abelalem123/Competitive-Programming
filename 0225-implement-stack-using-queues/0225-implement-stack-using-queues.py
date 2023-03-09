class MyStack:

    def __init__(self):
        self.q1=[]
        self.q2=[]
    def push(self, x: int) -> None:
        if not self.q1:
            self.q1.append(x)
        else:
            self.q2=self.q1
            self.q1=[]
            self.q1.append(x)
            for i in self.q2:
                self.q1.append(i)

    def pop(self) -> int:
        return self.q1.pop(0)
    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()