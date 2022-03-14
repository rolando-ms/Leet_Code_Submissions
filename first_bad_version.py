class Solution:
    def __init__(self):
        self.min = 0
        # self.max = -1

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.min == 0:
            self.min = 1
            # self.max = n

        avg_num = int((n + self.min) / 2)
        if n - self.min == 0:
            # self.max = n
            return n
        elif isBadVersion(avg_num):
            #n = avg_num
            return self.firstBadVersion(avg_num)
        elif n - self.min == 1:
            # self.max = n
            return n
        else:
            self.min = avg_num
            return self.firstBadVersion(n)
        # return self.max

def isBadVersion(num):
    return True

sol = Solution()
x = sol.firstBadVersion(5)
print(x)