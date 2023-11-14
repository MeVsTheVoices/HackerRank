from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for edge in edges:
            src1, dest1 = edge
            src2, dest2 = edge[::-1]
            graph[src1].append(dest1)
            graph[src2].append(dest2)

        visited = set()
        def findPath(node):
            if node == destination:
                return True
            visited.add(node)
            for adjacent in graph[node]:
                if adjacent not in visited:
                    if findPath(adjacent):
                        return True
            return False
        return findPath(source)