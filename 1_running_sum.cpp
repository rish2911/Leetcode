#include <iostream>
#include <vector>

class Solution {
public:

    std::vector<int> runningSum(std::vector<int>& nums) 
    {
     // std::vector<int> sum;
 
     for (int i; i<nums.size();i++)
     {
         if (i>0)
         {
         nums[i]+=nums[i-1];
            }
      
     }   
    return nums;   
    }
};