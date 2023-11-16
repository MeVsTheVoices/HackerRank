from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        source = 0
        destination = len(graph) - 1
        workingPaths, targetPaths = [[0]], []
        while workingPaths:
            # Use list as a stack
            currentPath = workingPaths.pop(0)
            # Take the last visited node from path
            edges = graph[currentPath[-1]]
            # If there's no more paths from this node
            if not edges:
                # Disreguard the path
                continue
            for edge in edges:
                if edge == destination:
                    # Here if we've found a path
                    targetPaths.append(currentPath + [edge])
                else:
                    # Here if we haven't, but, there's more to examine
                    workingPaths = [workingPaths + [edge]] + workingPaths
        return targetPaths