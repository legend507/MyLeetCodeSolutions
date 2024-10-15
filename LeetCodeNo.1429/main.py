class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = nums
        self.store = {}
        for i in nums:
            self.store[i] = self.store.get(i, 0) + 1

    def showFirstUnique(self) -> int:
        for i in self.queue:
            if self.store.get(i, 0) == 1:
                return i
        return -1

    def add(self, value: int) -> None:
        self.queue.append(value)
        self.store[value] = self.store.get(value, 0) + 1

from collections import deque

class FirstUnique_slow:
    # This is editorial solution,
    # But it's slower than my solution.
    def __init__(self, nums: List[int]):
        self._queue = deque(nums)

    def showFirstUnique(self):
        for item in self._queue:
            if self._queue.count(item) == 1:
                return item
        return -1

    def add(self, value):
        self._queue.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)