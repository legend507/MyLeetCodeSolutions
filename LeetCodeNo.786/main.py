from heapq import heappush, heappop

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # Aka. priority queue, FIFO, ascending by default.
        minHeap = []
        N = len(arr)
        
        # Populate min heap with fractions.
        # Bigger fraction will be deep in the queue.
        for i in range(N):
            for j in range(i + 1, N):
                fraction = (arr[i] / arr[j], [arr[i], arr[j]])
                heappush(minHeap, fraction)
        
        # Pop k-1 smallest fractions.
        for _ in range(k - 1):
            heappop(minHeap)
        
        # Return the k-th smallest fraction
        return heappop(minHeap)[1]
    