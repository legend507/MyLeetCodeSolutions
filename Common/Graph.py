# Implement graph using matrix.

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

    def dfs(self, start_vertex_data):
        visited = [False] * self.size
        start_vertex = self.vertex_data.index(start_vertex_data)
        self.dfs_util(start_vertex, visited)

class DirectionalGraph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size  

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            #self.adj_matrix[v][u] = 1

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

    def dfs(self, start_vertex_data):
        visited = [False] * self.size

        start_vertex = self.vertex_data.index(start_vertex_data)
        self.dfs_util(start_vertex, visited)
        
    def bfs(self, start_vertex_data):
        queue = [self.vertex_data.index(start_vertex_data)]
        visited = [False] * self.size
        visited[queue[0]] = True
        
        while queue:
            current_vertex = queue.pop(0)
            print(self.vertex_data[current_vertex], end=' ')
            
            for i in range(self.size):
                if self.adj_matrix[current_vertex][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

class Solution:
    def minimumDistance(
        self, 
        n: int, # size of the graph
        edges: list[list[int]], # directional edges
        s: int, # starting node
        marked: list[int] # destination nodes (can have multiple destinations).
    ) -> int:
        from collections import defaultdict
        import heapq
        # Editorial solution :Dijkstra's Algorithm

        # Convert marked array to set for O(1) lookups
        mark_set = set(marked)

        # Build adjacency list representation of the graph
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))

        # Distance dictionary initialized only for `s`
        dist = {s: 0}

        # Min heap prioritized by distance
        min_heap = [(0, s)]

        # Dijkstra's algorithm
        while min_heap:
            distance, node = heapq.heappop(min_heap)

            # Found a marked node, return its distance
            if node in mark_set:
                return dist[node]

            # Explore neighbors
            for next_node, weight in adj[node]:
                new_dist = distance + weight

                # If we found a shorter path, update and add to the priority queue
                if new_dist < dist.get(next_node, float("inf")):
                    dist[next_node] = new_dist
                    heapq.heappush(min_heap, (new_dist, next_node))

        # No path found to any marked node
        return -1
