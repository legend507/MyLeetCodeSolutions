
# Heap queue, aka priority queue.
# Heaps are binary trees for which every parent node has a value less than or equal to any of its children.
from heapq import heapify, heappop, heappush

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        h = [(t, t, 1) for i, t in enumerate(workerTimes)]
        print(h)
        heapify(h)
        print(h)
        while mountainHeight > 1:
            ps, wt, x = heappop(h)
            heappush(h, (ps + wt * (x + 1), wt, x + 1))
            mountainHeight-= 1
        return heappop(h)[0] 

s = Solution()
print(s.minNumberOfSeconds(5, [1, 5]))