class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        if n == 1:
            return ["1"]
        l = Solution.fizzBuzz(self, n - 1)
        if n % 3 ==0 and n % 5 == 0:
            l.append("FizzBuzz")
        elif n % 3 == 0:
            l.append("Fizz")
        elif n % 5 == 0:
            l.append("Buzz")
        else:
            l.append(str(n))
        return l

s = Solution()
print(s.fizzBuzz(15))