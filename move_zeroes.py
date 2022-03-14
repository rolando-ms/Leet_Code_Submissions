class Solution:
    def moveZeroes(self, nums):
        zeroes_count = 0
        for i in range(len(nums)):
            if nums[i - zeroes_count] == 0:
                nums.append(nums.pop(i - zeroes_count))
                zeroes_count += 1
            # if i == len(nums) - zeroes_count:
            #     break
        return nums

sol = Solution()
nums = [0,1,0,3,12]
# nums = [0,0,1]
nums = [0]
nums = [-58305,-22022,0,0,0,0,0,-76070,42820,48119,0,95708,-91393,60044,0,-34562,0,-88974]
print(sol.moveZeroes(nums))