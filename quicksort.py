
class Solution:
    def __init__(self):
        self.nums = []

    def sortedSquares(self, nums):
        self.nums = nums
        for i in range(len(self.nums)):
            self.nums[i] = self.nums[i]**2
        self.quicksort(0, len(self.nums)-1)
        return self.nums

    def quicksort(self, low, high):
        if low < high:
            pivot = self.partition(low, high) #int((high + low) / 2)
            self.quicksort(low, pivot - 1)
            self.quicksort(pivot + 1, high)

    def partition(self, low, high):
        pivot_idx = int((high + low) / 2)
        # pivot_idx = high
        pivot_num = self.nums[pivot_idx]
        partition_idx = low
        self.nums.pop(pivot_idx)
        for i in range(low, high):
            if self.nums[i] <= pivot_num and partition_idx != i:
                aux = self.nums[partition_idx]
                self.nums[partition_idx] = self.nums[i]
                self.nums[i] = aux
                partition_idx += 1
            elif self.nums[i] <= pivot_num:
                partition_idx += 1

            if i == high-1:
                self.nums.insert(partition_idx, pivot_num)
        return partition_idx

nums = [-4,-1,0,3,10]
# nums = [-7,-3,2,3,11]
# nums = [1]
sol = Solution()
print(sol.sortedSquares(nums))