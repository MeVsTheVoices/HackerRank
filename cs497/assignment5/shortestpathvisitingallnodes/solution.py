class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = queue.Queue()
        visited = set()
        for i in range(n):
            q.put((i, 1 << i, 0))
            visited.add((i, 1 << i))

        while not q.empty():
            node, state, dist = q.get()
            if state == (1 << n) - 1:
                return dist
            for neighbor in graph[node]:
                if (neighbor, state | (1 << neighbor)) not in visited:
                    q.put((neighbor, state | (1 << neighbor), dist + 1))
                    visited.add((neighbor, state | (1 << neighbor)))
        return -1

