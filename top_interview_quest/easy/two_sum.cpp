class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i=0;i<nums.size();i++) {
        int rem = target - nums.at(i);
        auto it = find(nums.begin(), nums.end(), rem);
        int ind = int(it-nums.begin());
        if ((it!=nums.end())&&(ind!=i)) {
            
            return {ind,i};
        }
        }
         
        
    return {};}
};