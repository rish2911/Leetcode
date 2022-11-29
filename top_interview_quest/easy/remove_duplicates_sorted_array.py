class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        k=0
        l = len(nums)
        while k!=len(nums):
          if nums[j] in nums[:j]:
              temp = nums[j]
              nums.pop(j)
              nums.append(temp)
          else:
              j+=1
          k+=1
        return j



##another s=way

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        insertIndex = 1
        for i in range(1, size):
            # Found unique element
            if nums[i - 1] != nums[i]:      
                # Updating insertIndex in our main array
                nums[insertIndex] = nums[i] 
                # Incrementing insertIndex count by 1 
                insertIndex = insertIndex + 1       
        return insertIndex