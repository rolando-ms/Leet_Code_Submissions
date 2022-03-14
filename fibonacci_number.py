# class Solution:
#     def fib(self, n: int) -> int:
#         f0 = 0
#         f1 = 1
#         fn = 0
#         if n == 0:
#             return f0
#         elif n == 1:
#             return f1
#         else:
#             for i in range(n-1):
#                 fn = f1 + f0
#                 f0 = f1
#                 f1 = fn
#         return fn

class Solution:
    def fib(self, n: int) -> int:
        series = [0, 1, 1]
        if n < 3:
            return series[n]
        else:
            series = [0] * (n + 1)
            series[0] = 0
            series[1] = 1
            series[2] = 1
            for i in range(3, n+1):
                series[i] = series[i-1] + series[i-2]
            return series[n]

sol = Solution()
print(sol.fib(5))