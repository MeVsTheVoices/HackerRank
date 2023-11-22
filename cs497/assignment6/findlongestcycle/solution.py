from collections import deque
from typing import List

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        inDegrees = [0 for _ in edges]
        visited = [False for _ in edges]

        for edge in edges:
            if edge != -1:
                inDegrees[edge] += 1
        
        rootNodes = deque()

        for i in range(len(edges)):
            if inDegrees[i] == 0:
                rootNodes.append(i)
        
        while rootNodes:
            node = rootNodes.popleft()
            visited[node] = True
            nodeVisits = edges[node]
            if nodeVisits != -1:
                inDegrees[nodeVisits] -= 1
                if inDegrees[nodeVisits] == 0:
                    rootNodes.append(nodeVisits)
        
        ret = -1
        for i in range(len(edges)):
            if not visited[i]:
                nodeVisits = edges[i]
                count = 1
                visited[i] = True
                while nodeVisits != i:
                    visited[nodeVisits] = True
                    count += 1
                    nodeVisits = edges[nodeVisits]
                ret = max(ret, count)
        return ret

