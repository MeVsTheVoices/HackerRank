class Solution:
    def fib(self, n: int) -> int:
        def doFib(n):
            i, j = 0, 1
            for _ in range(n + 1):
                yield i
                i, j = j, i + j

        res = list(doFib(n))
        return res[-1]