# Testing
Testing is at python_testing/findallpaths_test.py

# Intuition
We're reusing the same methodology as seen in other solutions. We avoid recursion here because it isn't necessary, instead, we simply treat a list as a queue and pop from the end of it. We also avoid using a set to track visited nodes because we're only interested in paths that end at the destination node.

# Approach
    - Create a queue of paths, starting with the source node
    - While the queue is not empty:
        - Pop a path from the queue
        - Get the edges of the last node in the path
        - For each edge:
            - If the edge is the destination node:
                - Add the path to the list of valid paths
            - Else:
                - Add the path to the queue

# Complexity
- Time complexity: O(n^2)
  - In the worst case, were every node to point to every other node, we would have to iterate over every node in the graph for every node in the graph.

- Space complexity: O(n^2)
  - In the worst case, were every node to point to every other node, we would have to store every node in the graph for every node in the graph.

# Code
```
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

        
```