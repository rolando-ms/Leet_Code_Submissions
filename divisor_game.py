# class Solution:
#     def __init__(self):
#         self.alice_turn = True
#
#     def divisorGame(self, n: int) -> bool:
#         if n < 2:
#             if self.alice_turn:
#                 return False
#             else:
#                 return True
#
#         for i in range(2, n+1):
#             if n % int(n/i) == 0:
#                 n -= int(n / i)
#                 self.alice_turn = not self.alice_turn
#                 break
#         return self.divisorGame(n)

class Solution:
    """
    Subtract 1 from n and recursively go to base case (n = 1 or 0)
    """
    def __init__(self):
        self.alice_turn = True

    def divisorGame(self, n: int) -> bool:
        if n < 2:
            if self.alice_turn:
                return False
            else:
                return True

        for i in range(1, n + 1):
            if n % int(n / i) == 0:
                n -= i
                self.alice_turn = not self.alice_turn
                break
        return self.divisorGame(n)

sol = Solution()
print(sol.divisorGame(4))