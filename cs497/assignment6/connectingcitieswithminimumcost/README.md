# Testing
Testing is at ppython_testing/connectingcitieswithminimumcost_test.py

# Intuition
We're going to modify some code we wrote recently as we can be certain of its correctness. We modify the code from find all paths to take parameters for the source and destination nodes. As our graph is bidirectional we create two maps for each node, one for the edges going out and one for the edges coming in. We then iterate over every node in the graph and find all paths from that node to every other node. We then iterate over every path and find the minimum cost.


# Approach
- Build the graph
    - Iterate over every connection and add it to the graph
    - We store the weight of the edge as well
    - We store the edge in both directions as the graph is bidirectional
    - We store the edges in a list of tuples, where the first element is the node and the second element is the weight
- Find all paths
- Iterate over every node in the graph
    - Iterate over every other node in the graph
        - Find all paths from the current node to the other node
        - Add the path to the list of paths
- Find the minimum cost
    - Iterate over every path
        - Iterate over every edge in the path
            - Accumulate the weight of the edges
        - If the cost is less than the current minimum cost, set the minimum cost to the current cost


# Complexity
- Time complexity: O(n^2)
    - In the worst case, were every node to point to every other node, we would have to iterate over every node in the graph for every node in the graph.

- Space complexity: O(n^2)
    - We keep two maps of size n, one for the graph and one for the paths. In the worst case, we would have to store every path from every node to every other node, which would be n^2.

# Code
```
from typing import List

class Solution:
    def connectAllCities(self, n: int, connections: List[List[int]]) -> int:
        # Build the graph
        graph = {}
        for connection in connections:
            if connection[0] not in graph:
                graph[connection[0]] = []
            if connection[1] not in graph:
                graph[connection[1]] = []
            graph[connection[0]].append((connection[1], connection[2]))  # Store the weight as well
            graph[connection[1]].append((connection[0], connection[2]))  # Store the weight as well
        
        # Find all paths
        all_paths = []
        for start in graph.keys():
            for end in graph.keys():
                if start != end:
                    paths = self.allPathsSourceTarget(graph, start, end)
                    for path in paths:
                        if path not in all_paths:
                            all_paths.append(path)
        
        # Find the minimum cost
        min_cost = 0
        for path in all_paths:
            cost = 0
            for i in range(len(path)-1):
                cost += path[i][1]  # Accumulate the weight of the edges
            if min_cost == 0 or cost < min_cost:
                min_cost = cost
        
        return min_cost
    
    def allPathsSourceTarget(self, graph: List[List[int]], source, destination) -> List[List[int]]:
        validPaths = []
        queue = [[(source, 0)]]  # Initialize the queue with the source and weight 0

        while queue:
            path = queue.pop(len(queue) - 1)
            edges = graph[path[-1][0]]
            
            for edge in edges:
                if edge[0] == destination:
                    validPaths.append(path + [edge])
                elif edge[0] not in [p[0] for p in path]:
                    queue.append(path + [edge])
        return validPaths
```