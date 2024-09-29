class AllOne:

    def __init__(self):
        self.store = {}

    def inc(self, key: str) -> None:
        self.store[key] = self.store.get(key, 0) + 1

    def dec(self, key: str) -> None:
        self.store[key] -= 1
        if self.store[key] == 0:
            del self.store[key]
        
    def getMaxKey(self) -> str:
        return max(self.store, key=self.store.get) if self.store else ""
        
    def getMinKey(self) -> str:
        return min(self.store, key=self.store.get) if self.store else ""

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()