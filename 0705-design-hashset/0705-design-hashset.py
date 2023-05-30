class MyHashSet:


    def __init__(self):
        self.s=defaultdict(int)
    def add(self, key: int) -> None:
        self.s[key]=1
    def remove(self, key: int) -> None:
        if key in self.s:
            del self.s[key]

    def contains(self, key: int) -> bool:
        return key in self.s


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)