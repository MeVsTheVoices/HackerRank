class Solution:
    def myAtoi(self, s: str) -> int:
        MIN_INT = -pow(2, 31)
        MAX_INT = pow(2, 31) - 1
        stripped = s.strip()
        if len(stripped) < 1:
            return 0
        positive = True
        position = 0
        if stripped[0] == '+':
            positive = True
            position += 1
        elif stripped[0] == '-':
            positive = False
            position += 1
        elif not stripped[0].isnumeric():
            return 0
        power = 0
        value = 0
        for i in range(len(stripped) - 1, position - 1, -1):
            character = stripped[i]
            if character.isnumeric():
                value += pow(10, power) * int(character)
                power += 1
            else:
                power = 0
                value = 0
        value = value if positive else -value
        if value < MIN_INT:
            value = MIN_INT
        elif value > MAX_INT:
            value = MAX_INT
        return value