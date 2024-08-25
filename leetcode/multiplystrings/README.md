# Intuition
Just doing long multiplication, just as you would on paper

# Approach
I like the larger term on top, so, we swap them if necessary. From then, we take, from the right, one digit of the bottom, then multiply that by the top, carrying the one if necessary, and multiplying the result by an increasing power of ten. We convert that to a string, then return the result.

# Complexity
- Time complexity: O(n^m)

- Space complexity: O(1)

# Code
```python3 []
class Solution:
    def multiplyHelper(self, top: str, bottom: str, multiple : int):
        bInt = int(bottom)
        s = 0
        carried = False
        for i in range(len(top) - 1, -1, -1):
            val = int(top[i]) * bInt
            if carried:
                val += 1
                carried = False
            if val > 9:
                val -= 10
                carried = True
            s += val * multiple
            multiple *= 10
        if carried:
            s += multiple
        return s

    def multiply(self, num1: str, num2: str) -> str:
        larger, smaller = 0, 0
        if len(num1) > len(num2):
            larger, smaller = num1, num2
        else:
            larger, smaller = num2, num1
        multiple = 1
        s = 0
        for v in smaller[::-1]:
            print(str(larger) + " " + str(v) + " " + str(multiple))
            b = self.multiplyHelper(larger, v, multiple)
            print(b)
            s += b
            multiple *= 10
        return str(s)


```