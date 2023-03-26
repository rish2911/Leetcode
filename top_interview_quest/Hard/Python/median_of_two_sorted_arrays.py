class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        r,l = 0,0 #pointer to nums  list
        dummy = []
        for i in range(total_len):
            if r<len(nums2) and l<len(nums1):
                if nums1[l]<nums2[r] or nums1[l]==nums2[r]:
                    dummy.append(nums1[l])
                    l+=1
                else:
                    dummy.append(nums2[r])
                    r+=1
            elif r==len(nums2):
              dummy[i:] = nums1[l:]
              break
            else:
               dummy[i:] = nums2[r:]
               break
        if total_len%2==0:
            return (dummy[int(total_len/2)]+dummy[int(total_len/2)-1])/2
        else:
            return (dummy[int(total_len/2)])