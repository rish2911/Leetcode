class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tsum = [0,sum(nums)]
        for i in range(len(nums)):
            if i>0:
                tsum[0]+=nums[i-1]
            tsum[1]-=nums[i]
            if tsum[0]==tsum[1]:
                return i
        return -1
        
