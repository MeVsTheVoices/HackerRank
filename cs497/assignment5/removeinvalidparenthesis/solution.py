from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def toBeRemoved(s):
            openingToBeRemoved = 0
            closingToBeRemoved = 0
            for c in s:
                if c == '(':
                    openingToBeRemoved += 1
                elif c == ')':
                    if openingToBeRemoved > 0:
                        openingToBeRemoved -= 1
                    else:
                        closingToBeRemoved += 1
            return openingToBeRemoved, closingToBeRemoved
        
        def noneToBeRemoved(s):
            openingToBeRemoved, closingToBeRemoved = toBeRemoved(s)
            return not openingToBeRemoved and not closingToBeRemoved
        
        result = {}
        def buildRecursively(s, index, opening, closing, 
                             openingToBeRemoved, closingToBeRemoved, expressionSoFar):
            if index == len(s):
                if openingToBeRemoved == 0 and closingToBeRemoved == 0:
                    ans = "".join(expressionSoFar)
                    result[ans] = 1
            else:
                if ((s[index] == '(' and (openingToBeRemoved > 0)) or
                    ((s[index] == ')') and (closingToBeRemoved > 0))):
                    buildRecursively(s, index + 1,
                                     opening, closing,
                                     openingToBeRemoved - (s[index] == '('),
                                     closingToBeRemoved - (s[index] == ')'),
                                     expressionSoFar)
                    
                expressionSoFar.append(s[index])

                if s[index] != '(' and s[index] != ')':
                    buildRecursively(s, index + 1,
                                    opening, closing,
                                    openingToBeRemoved, closingToBeRemoved,
                                    expressionSoFar)
                elif s[index] == '(':
                    buildRecursively(s, index + 1,
                                    opening + 1, closing,
                                    openingToBeRemoved, closingToBeRemoved,
                                    expressionSoFar)
                elif s[index] == ')' and opening > closing:
                    buildRecursively(s, index + 1,
                                    opening, closing + 1,
                                    openingToBeRemoved, closingToBeRemoved,
                                    expressionSoFar)
                    
                expressionSoFar.pop()

        openingToBeRemoved, closingToBeRemoved = toBeRemoved(s)
        buildRecursively(s, 0, 0, 0, openingToBeRemoved, closingToBeRemoved, [])

        return list(result.keys())
                
        
