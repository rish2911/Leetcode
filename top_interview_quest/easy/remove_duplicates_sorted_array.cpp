class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int siz = nums.size();
        int ind = 1; 
        for (int i=1;i<siz;i++) {
                if (nums[i]!=nums[i-1]) {
                    nums[ind] = nums[i];
                    ind++;
                }
            } 
        return ind; }
};


//alternate
class Solution 
{
public:
    int removeDuplicates(vector<int>& nums, int k = 1)
    {
		return distance(nums.begin(), unique(nums.begin(), nums.end()));
		// or just subtract iterators...
		// return unique(nums.begin(), nums.end()) - nums.begin();
    }
};