from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        source = 0
        destination = len(graph) - 1

        validPaths = []
        queue = [[source]]

        while queue:
            path = queue.pop(len(queue) - 1)
            edges = graph[path[-1]]
            
            for edge in edges:
                if edge == destination:
                    validPaths.append(path + [edge])
                else:
                    queue.append(path + [edge])
        return validPaths

        