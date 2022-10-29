class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string com;
        std::sort(strs.begin(), strs.end());
        
        com = strs.at(0);

            
        for (int i=0;i<strs.at(0).length();i++) {
              for (int j=0;j<strs.size();j++) {
                  if (com[i]!=(strs.at(j).at(i))) {
                      return com.substr(0,i);
                  }
              }
        }
        
    return com;}
};