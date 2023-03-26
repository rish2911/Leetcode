class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int total_len = nums1.size() + nums2.size();
        // std::cout<<total_len;
        int l= 0;
        int r = 0;
        vector<int> dummy(total_len);
        for (int i=0;i<total_len;i++ ) {
            if (l<nums1.size() && r<nums2.size()) {
                if (nums1.at(l)<nums2.at(r) || (nums1.at(l)==nums2.at(r))) {
                    dummy.insert(dummy.begin()+i,nums1.at(l));
                    l++; 
                }
                else {
                    dummy.insert(dummy.begin()+i,nums2.at(r));
                    r++;
                }
                }
            else if (l==nums1.size()) {
                dummy.insert(dummy.begin()+i,nums2.begin()+r, nums2.end());
                break;
            }
            else  {
                dummy.insert(dummy.begin()+i,nums1.begin()+l, nums1.end());
                break;
            }
        }
        int id = int(total_len/2);
        std::cout<<id;
        if (total_len%2==0) {
            return double((dummy.at(id-1) + dummy.at(id)))/2;
        }
        else {
            return (dummy.at(id));
        }
        } 
};