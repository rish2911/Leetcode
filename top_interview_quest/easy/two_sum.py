class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)%2==0:
            r = int((len(nums)/2)+1)
        else:
            r = int((len(nums)+1)/2)
        for i in range(r):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j]==target:
                    return [i,j]
                elif  ((len(nums)-1-i)>i):
                    if nums[-1-i] + nums[j] == target:
                        return [len(nums)-1-i, j]