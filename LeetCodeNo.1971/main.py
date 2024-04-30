class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        # Only 1 vertrex.
        if n == 1:
            return True
        
        visited = [False] * n
        visited[source] = True
        flag = True
        while flag:
            flag = False
            for edge in edges:
                # If either of the vertex is a True.
                if visited[edge[0]] != visited[edge[1]]:
                    visited[edge[0]] = True
                    visited[edge[1]] = True
                    flag = True
                if visited[destination]:
                    return True
        return False
                
