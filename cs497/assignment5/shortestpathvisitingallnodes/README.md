# Intuition
We use BFS to find the shortest path. We use a tuple (node, state) to represent the state of the BFS. The state is a bit mask of the nodes we have visited. We use a set to store the visited states. We use a queue to store the states to be visited. We start from each node and add it to the queue. We also add the state of the node to the visited set. We keep track of the distance from the start node. We keep adding the neighbors of the current node to the queue if the state of the neighbor is not in the visited set. We also add the state of the neighbor to the visited set. We return the distance when we find a state that has visited all the nodes.

# Approach
    - Initialize a queue, a set, and a distance variable.
    - For each node in the graph:
        - Add the node, the state of the node, and the distance to the queue.
        - Add the state of the node to the set.
    - While the queue is not empty:
        - Get the node, the state, and the distance from the queue.
        - If the state is equal to (1 << n) - 1:
            - Return the distance.
        - For each neighbor of the node:
            - If the state of the neighbor is not in the set:
                - Add the neighbor, the state of the neighbor, and the distance + 1 to the queue.
                - Add the state of the neighbor to the set.
    - Return -1.

# Complexity
- Time complexity: O(2^n)

- Space complexity: O(n)

# Code
```
import queue
from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = queue.Queue()
        visited = set()
        for i in range(n):
            q.put((i, 1 << i, 0))
            visited.add((i, 1 << i))

        while not q.empty():
            node, state, dist = q.get()
            if state == (1 << n) - 1:
                return dist
            for neighbor in graph[node]:
                if (neighbor, state | (1 << neighbor)) not in visited:
                    q.put((neighbor, state | (1 << neighbor), dist + 1))
                    visited.add((neighbor, state | (1 << neighbor)))
        return -1
        


        


```