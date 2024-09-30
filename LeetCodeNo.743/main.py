# 743. Network Delay Time
# BFS search a graph.

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # time.
        time = [-1 for _ in range(n + 1)]
        time[k] = 0

        # Re-construct the times list to a dict, with key = source node, value = [[dest_node_1, time_1], [dest_node_2, time_2], ...].
        edge_map = {}
        for i in times:
            edge_map[i[0]] = edge_map.get(i[0], [])
            edge_map[i[0]].append([i[1], i[2]])
        
        # Use a stack to store the nodes to spread to, starting from k.
        # Append a new node if the node hasn't been reached before, or new time is smaller than the old reach time.
        to_spread = [k]
        while to_spread:
            current_node = to_spread.pop(0)
            current_time = time[current_node]
            if current_node in edge_map:
                for edge in edge_map[current_node]:
                    dest = edge[0]
                    time_needed = edge[1]
                    dest_time = current_time + time_needed
                        
                    if dest_time < time[dest] or time[dest] == -1:
                        time[dest] = dest_time
                        to_spread.append(dest)

        time = time[1:]
        print(time)
        return max(time) if min(time) != -1 else -1
