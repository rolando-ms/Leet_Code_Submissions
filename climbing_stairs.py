import math

# class Solution():
#     def __init__(self):
#         self.ones = -1
#         self.twos = 0
#         self.steps = 1
#
#     def climbStairs(self, n: int) -> int:
#         if self.ones == -1:
#             self.ones = n
#
#         if n == 1:
#             return int(self.steps)
#
#         if self.ones / 2 < 1:
#             return int(self.steps)
#         else:
#             self.ones -= 2
#             self.twos += 1
#             self.steps += math.factorial(self.ones + self.twos) / (math.factorial(self.ones) * math.factorial(self.twos))
#             return self.climbStairs(n)

class Solution():
    def climbStairs(self, n: int) -> int:
        ones = n
        twos = 0
        steps = 1
        while(True):
            if ones > 1:
                ones -= 2
                twos += 1
                steps += math.factorial(ones + twos) / (math.factorial(ones) * math.factorial(twos)) # Possible permutations
            else:
                break
        return int(steps)

# 1836311903
sol = Solution()
print(sol.climbStairs(45))