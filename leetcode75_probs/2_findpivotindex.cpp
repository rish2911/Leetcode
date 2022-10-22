#include <iostream>
#include <vector>
class Solution {
public:
    int pivotIndex(std::vector<int>& nums) {
        int suml = 0;
        int sumr = 0;

        for (std::vector<int>::iterator it = nums.begin(); it!= nums.end(); ++it) {
            sumr+= *it;
        }
        for (int i=0;i<nums.size();i++) {
            if (i>0) {
                suml+=nums.at(i-1);
            }
            sumr-=nums.at(i);
            std::cout<<sumr<<suml<<std::endl;
            
            if (suml==sumr) {
                return i;
            }
        }
        
        return -1;
            
        
    }
};


int main() {
    Solution sol;

    std::vector<int> input{1,7,3,6,5,6};

    std::cout<<sol.pivotIndex(input);
}