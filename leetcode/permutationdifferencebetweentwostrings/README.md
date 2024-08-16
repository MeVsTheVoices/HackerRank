# Intuition
Just loop through both simultaneously to get the indexes

# Approach
Go through both strings simultaneously, store the index for each value.
Then come back around and for each value in the left hand side string, we look up the indexes it was found at, absolute value the difference, and add that to a sum.

# Complexity
- Time complexity: O(n)

- Space complexity: O(n)

# Code
```
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sIndices = {}
        tIndices = {}
        for (iIndex, i), (jIndex, j) in zip(enumerate(s), enumerate(t)):
            sIndices[i] = iIndex
            tIndices[j] = jIndex
        
        permDifference = 0
        for i in s:
            permDifference += abs(sIndices[i] - tIndices[i])
        
        return permDifference

```