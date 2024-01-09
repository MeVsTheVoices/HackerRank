# Intuition
Using a python generator to generate the fibonacci sequence, then return the last element of the sequence.

# Approach
- Use a generator to generate the fibonacci sequence
- Convert the generator to a list
- Return the last element of the list

# Complexity
- Time complexity: O(n)

- Space complexity: O(n)

# Code
```
class Solution:
    def fib(self, n: int) -> int:
        def doFib(n):
            i, j = 0, 1
            for _ in range(n + 1):
                yield i
                i, j = j, i + j

        res = list(doFib(n))
        print(res)
        return res[-1]
```