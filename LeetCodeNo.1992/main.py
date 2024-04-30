class Solution:
    def findFarmland(self, land):
        result = []
        m, n = len(land), len(land[0])
        
        def findFarmlandCoordinates(row, col):
            # Starting from this farmland, try to find left-top and right-bottom points.
            coordinates = [row, col]
            r, c = row, col
            
            # Find the right most row index.
            while r < m and land[r][col] == 1:
                r += 1
            # Find the bottom index.
            while c < n and land[row][c] == 1:
                c += 1
            
            # Append multiple elements to coordinates.
            coordinates.extend([r - 1, c - 1])
            
            # Set traversed farmland to 0.
            for i in range(row, r):
                for j in range(col, c):
                    land[i][j] = 0
            
            return coordinates
        
        for i in range(m):
            for j in range(n):
                # If found a 1, then there must be a farmland here, therefore a result to be appended.
                if land[i][j] == 1:
                    result.append(findFarmlandCoordinates(i, j))
        
        return result