from typing import *

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
