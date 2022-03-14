class Solution:
    def countBits(self, n: int):
        result = []
        for i in range(n+1):
            counter = 0
            for item in bin(i):
                if item == "1":
                    counter += 1
            result.append(counter)
        return result

sol = Solution()
print(sol.countBits(5))