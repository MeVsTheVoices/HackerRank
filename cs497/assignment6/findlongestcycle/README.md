# Testing
Testing is at python_testing/findlongestcycle_test.py

# Intuition
We use topological sort here. We erradicate all nodes with no incoming edges, and then we erradicate all nodes that have no incoming edges after that. We continue this until we have no nodes left. We then iterate through the nodes that we have not visited, and we find the longest cycle that we can find.

# Approach
    - We create an array of inDegrees, and we create an array of visited nodes.
    - We iterate through the edges, and we increment the inDegree of the node that the edge points to.
    - We create a queue of nodes that have no incoming edges.
    - We iterate through the queue, and we erradicate the node from the graph.
    - We then iterate through the nodes that we have not visited, and we find the longest cycle that we can find.

# Complexity
- Time complexity: O(n)
    - We iterate through the edges once, and we iterate through the nodes once.

- Space complexity: O(n)
    - We create an array of inDegrees, and we create an array of visited nodes. 

# Code
```
from collections import deque

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


```