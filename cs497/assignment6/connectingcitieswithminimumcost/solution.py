from typing import List

class Solution:
    def connectAllCities(self, n: int, connections: List[List[int]]) -> int:
        def lookup(x):
            if x != parents[x]:
                parents[x] = lookup(parents[x])
            return parents[x]
        
        connections.sort(key=lambda x: x[2])
        parents = list(range(n))

        totalCost = 0
        for source, destination, cost in connections:
            source, destination = source - 1, destination - 1
            if lookup(source) == lookup(destination):
                continue
            else:
                totalCost += cost
                parents[lookup(source)] = lookup(destination)
                n -= 1
            if n == 1:
                return totalCost
        return -1

