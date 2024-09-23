class Solution:
    # My solution, a bit slow.
    # Thoughts: use BFS to traverse matrix.
    def BFS(self, i, isConnected, in_province, provinces):
        from collections import deque

        queue = deque([i])

        this_province = []
        while queue:
            city = queue.popleft()
            this_province.append(city)
            in_province[city] = True
            for idx in range(0, len(isConnected)):
                if isConnected[city][idx] == 1 and idx not in this_province:
                    queue.append(idx)
        provinces.append(this_province)

    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        in_province = [False for _ in range(n)]
        provinces = []

        for i in range(n):
            if in_province[i] == False:
                self.BFS(i, isConnected, in_province, provinces)
        
        print(provinces)
        return len(provinces)
    
s = Solution()
s.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])