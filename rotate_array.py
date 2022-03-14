
# class Solution:
#     def rotate(self, nums, k):
#         for i in range(k):
#             last_num = nums.pop()
#             nums.insert(0,last_num)
#         return nums

# # This solution does not do in-place operations
# class Solution:
#     def rotate(self, nums, k):
#         nums_rotated = []
#         for i in range(k):
#             nums_rotated.append(nums.pop(len(nums) - k + i))
#         nums_rotated += nums
#         return nums_rotated #[*nums_rotated, *nums]

sol = Solution()
# nums = [1,2,3,4,5,6,7]
nums = [-1,-100,3,99]
print(sol.rotate(nums, 2))