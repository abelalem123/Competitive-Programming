class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache=defaultdict(int)
        self.linlist=deque()
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.linlist.remove(key)
        self.linlist.appendleft(key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.linlist.remove(key)
            self.linlist.appendleft(key)
            self.cache[key]=value
        else:
            if len(self.cache)==self.capacity:
                k=self.linlist.pop()
                del self.cache[k]
            self.linlist.appendleft(key)
            self.cache[key]=value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)