# Testing
Testing is at python_testing/validpath_test.py

# Intuition
The graph is bidirectional, so, first we create a list of lists, each list contains the nodes that are connected to the node at that index. Then, we use DFS to find a path from the source to the destination.

# Approach
    - Create a list of lists, each list contains the nodes that are connected to the node at that index.
    - Use DFS to find a path from the source to the destination.
    - If a path is found, return True, else return False.

# Complexity
- Time complexity: O(#Paths + #Nodes)

- Space complexity: O(#Paths)

# Code
```
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
```