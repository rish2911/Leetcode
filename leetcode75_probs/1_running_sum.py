class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i,j in enumerate(nums):
            if i>0:
                nums[i]=j+nums[i-1]
        return nums