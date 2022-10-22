class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        eligible = []
        for i in range(len(nums)):
            for a,j in enumerate(nums):
                if j<=target:
                    if j+nums[i] ==target and i !=a:
                        return [i,a]