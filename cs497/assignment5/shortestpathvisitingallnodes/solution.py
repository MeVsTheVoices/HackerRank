import queue
from bitArray import BitArray

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) <= 1:
            return 0
        
        # We use a bit array to keep track of the nodes we've visited
        # We also keep track of the number of nodes we've visited
        # and the number of nodes we've visited in total
        visited = BitArray(len(graph))
        visitedCount = 0
        totalVisited = 0

        # We use a queue to keep track of the nodes we've visited
        # and the number of nodes we've visited so far
        q = queue.Queue()
        q.put((0, visited, visitedCount))
        
        

