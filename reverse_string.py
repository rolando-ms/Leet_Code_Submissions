
class Solution:
    def reverseString(self, s):
        for i in range(len(s)):
            s.insert(i, s.pop())
        return s

sol = Solution()
s = ["H","a","n","n","a","h"]
print(sol.reverseString(s))