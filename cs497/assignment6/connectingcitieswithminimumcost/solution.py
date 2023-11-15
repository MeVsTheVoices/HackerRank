from typing import List

class Solution:
    def connectAllCities(self, connections: List[List[int]]) -> int:
        # Find the number of cities
        cities = set()
        for connection in connections:
            cities.add(connection[0])
            cities.add(connection[1])

        numberOfCities = len(cities)
        # Sort by minimum cost
        connections.sort(key = lambda x: x[2])



