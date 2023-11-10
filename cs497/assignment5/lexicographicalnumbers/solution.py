from typing import List

class Solution:
    def lexicalOrder(self, N: int) -> List[int]:
        ret = []

        def dfs(n):
            ret.append(n)

            for i in range(0, 10):
                if n * 10 + i <= N:
                    dfs(n * 10 + i)

        for i in range(1, 10):
            if i <= N:
                dfs(i)

        return ret