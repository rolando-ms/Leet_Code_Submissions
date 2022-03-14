class Solution:
    def __init__(self):
        self.t_0 = 0
        self.t_1 = 1
        self.t_2 = 1
        self.counter = 2

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return self.t_0
        elif n == 1:
            return self.t_1
        elif n == 2:
            return self.t_2
        elif self.counter != n:
            aux = self.t_2 + self.t_1 + self.t_0
            self.t_0 = self.t_1
            self.t_1 = self.t_2
            self.t_2 = aux
            self.counter += 1
            return self.tribonacci(n)
        else:
            return self.t_2

sol = Solution()
print(sol.tribonacci(25))