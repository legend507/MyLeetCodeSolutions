class LRUCache:
    # Thoughts: Use a dict to store data.
    # Use a list to store use history.
    # The key here is how to update this list based on get and put.

    def _update_history(self, key):
        to_evict = None
        # Update use history. A list storing used keys. 
        if key in self.use_history:
            self.use_history.remove(key)
            self.use_history.append(key)
        else:
            if len(self.use_history) == self.capacity:
                to_evict = self.use_history[0]
                self.use_history = self.use_history[1:]
                self.use_history.append(key)
            else:
                self.use_history.append(key)
        return to_evict

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}
        self.use_history = []

    def get(self, key: int) -> int:
        if key in self.use_history:
            _ = self._update_history(key)
        return self.store.get(key, -1)
        

    def put(self, key: int, value: int) -> None:
        to_evict = self._update_history(key)
        if to_evict != None:
            del self.store[to_evict]
        self.store[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)