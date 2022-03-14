class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sub_seq_idx = 0
        result = False
        if len(s) > 0:
            for i in range(len(t)):
                if s[sub_seq_idx] == t[i]:
                    sub_seq_idx += 1
                if sub_seq_idx == len(s) and sub_seq_idx > 0:
                    result = True
                    break
        else:
            result = True
        return result

sol = Solution()
s = "abc"
t = "ahbgdc"
# s = "b"
# t = "c"
# s = "acb"
# t = "ahbgdc"
print(sol.isSubsequence(s,t))