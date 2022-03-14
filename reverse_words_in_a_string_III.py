
class Solution:
    def reverseWords(self, s):
        s_list = s.split()
        for i in range(len(s_list)):
            s_list[i] = self.reverseString(s_list[i])
        return ' '.join(s_list)

    def reverseString(self, s):
        s_reversed = ''
        for i in range(len(s)):
            s_reversed += s[-1-i]
        return  s_reversed

sol = Solution()
s = "Let's take LeetCode contest"
s = "God Ding"
print(sol.reverseWords(s))