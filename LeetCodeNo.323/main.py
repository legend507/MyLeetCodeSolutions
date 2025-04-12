# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

# Return the number of connected components in the graph.

class NoDirectionalGraph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size  

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")

    def dfs_util(self, v, visited):
        visited[v] = True
        print(self.vertex_data[v], end=' ')

        for i in range(self.size):
            if self.adj_matrix[v][i] == 1 and not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start, visited):
        start_vertex = start
        self.dfs_util(start_vertex, visited)
        return visited

class Solution:
    # My solution. Worked but slow.
    def countComponents_my(self, n: int, edges: List[List[int]]) -> int:
        graph = NoDirectionalGraph(n)
        for edge in edges:
            graph.add_edge(edge[0], edge[1])

        visited = [False] * n
        count = 0
        for start in range(n):
            if visited[start] == False:
                count += 1
                visited = graph.dfs(start = start, visited=visited)
        
        return count