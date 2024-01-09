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