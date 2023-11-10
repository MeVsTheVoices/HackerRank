# Intuition
We use DFS to traverse the tree of all possible numbers. We start with 1, and then we try to append 0-9 to the end of it. If the number is less than or equal to N, we append it to the result and then recursively call the function on it. We do this for all numbers from 1 to 9.

# Approach
    - Initialize a list to store the result.
    - Define a function to do DFS.
        - Append the number to the result.
        - For each digit from 0 to 9:
            - If the number * 10 + digit is less than or equal to N:
                - Call the function on the number * 10 + digit.
    - For each number from 1 to 9:
        - If the number is less than or equal to N:
            - Call the function on the number.
    - Return the result.

# Complexity
- Time complexity: O(n)

- Space complexity: O(1)

# Code
```
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
```