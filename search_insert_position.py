class Solution:
    def __init__(self):
        self.min = 0
        self.max = -1

    def searchInsert(self, nums, target):

        if self.max == -1:
            self.max = len(nums) - 1

        if self.max - self.min == 0:
            if nums[self.min] > target:
                return self.min
            elif nums[self.max] == target or nums[self.max] > target:
                return self.max
            else:
                return self.max + 1

        avg = int((self.max + self.min) / 2)

        if nums[avg] == target:
            return avg
        elif self.max - self.min == 1:
            if nums[self.min] > target:
                return self.min
            elif nums[self.max] == target or nums[self.max] > target:
                return self.max
            else:
                return self.max + 1
        elif nums[avg] > target:
            self.max = avg
            return self.searchInsert(nums, target)
        else:
            self.min = avg
            return self.searchInsert(nums, target)

sol = Solution()
nums = [-5,-1,5,6]
target = 4
print(sol.searchInsert(nums, target))