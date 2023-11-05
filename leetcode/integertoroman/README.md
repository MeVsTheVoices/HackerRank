# Intuition
Use a dictionary and iterate through the keys in descending order. For each key, check if the number is greater than or equal to the key. If so, subtract the key from the number and add the value to the result string. Repeat until the number is 0.

# Approach
    - Create a dictionary with the roman numerals as keys and the corresponding values as values.
    - Iterate through the keys in descending order.
    - For each key, check if the number is greater than or equal to the key.
    - If so, subtract the key from the number and add the value to the result string.
    - Repeat until the number is 0.

# Complexity
- Time complexity: O(n)

- Space complexity: O(1)

# Code
```
class Solution:
    def intToRoman(self, num: int) -> str:
        map = {
            1000: "M", 900: "CM", 500: "D",
            400: "CD", 100: "C", 90: "XC",
            50: "L", 40: "XL", 10: "X",
            9: "IX", 5: "V", 4: "IV",
            1: "I"}

        res = ""

        for i in map:
            while (num // i) >= 1:
                num -= i
                res = res + map[i]

        return res
```