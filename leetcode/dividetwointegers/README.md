# Intuition
We simply keep adding the divisor by powers of two then subtract it from the dividend. The number of times we can subtract the divisor from the dividend is the quotient. We keep doing this until the dividend is less than the divisor.

# Approach
1. Check if the quotient is negative or positive.
2. If the quotient is negative, we need to convert the divisor and dividend to negative numbers.
3. We then keep subtracting the divisor from the dividend until the dividend is less than the divisor.
4. We keep track of the number of times we subtracted the divisor from the dividend. This is the quotient.

# Complexity
- Time complexity: O(log(n) * n)

- Space complexity: O(1)

# Code
```
# Remove the unused import statement for the "math" module
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1
        elif dividend == -2147483648 and divisor == -1: 
            return 2147483647
        divisor = -divisor if divisor < 0 else divisor
        dividend = -dividend if dividend < 0 else dividend
        quotient = 0
        while dividend >= divisor:
            powerOfTwo = 0
            while (divisor << powerOfTwo) <= dividend:
                powerOfTwo += 1
            quotient += 1 << (powerOfTwo - 1)
            dividend -= divisor << (powerOfTwo - 1)
        return -quotient if sign == -1 else quotient
```