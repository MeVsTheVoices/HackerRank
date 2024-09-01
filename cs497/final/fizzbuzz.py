from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
        # answer[i] == "Fizz" if i is divisible by 3.
        # answer[i] == "Buzz" if i is divisible by 5.
        # answer[i] == i (as a string) if none of the above conditions are true.
        # Input: n = 3
        # Output: ["1","2","Fizz"]
        # Input: n = 5
        # Output: ["1","2","Fizz","4","Buzz"]
        answer = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer