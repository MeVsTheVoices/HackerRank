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