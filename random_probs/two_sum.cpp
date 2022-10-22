#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    std::vector<int> twoSum(vector<int>& nums, int target) {
        
        for (int i=0; i<=nums.size(); ++i)
            for (int j=0; j<=nums.size(); ++j)
                if ((nums[j] + nums[i] == target) && (i!=j))
                {
                    return {i,j};
                }
               
    return {};}
};

int main()
{
std::vector<int> sample = {2,5,5,11};
Solution a;
std::vector<int> b = a.twoSum(sample, 10);
cout<<b;
return 0;
}
