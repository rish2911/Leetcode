class Solution {
public:
    bool isValid(string s) {
       vector<char> o_brackets {'(','{','['};
       vector<char> c_brackets {')','}',']'};
       vector<int> check;
       if (s.size()%2!=0) {
           return false;
       }
       for (int i = 0;i<s.size();i++) {
           auto it = find(o_brackets.begin(), o_brackets.end(), s[i]); 
           if (it!=o_brackets.end()) {
               int pos = (it - o_brackets.begin());
               check.push_back(pos);
           }
           else if (check.size()>0) {
               if (s[i]==c_brackets[check.back()]) {
                   check.pop_back();
               }
               else {
                   return false;
               }
           }
           else {
               return false;
           }
           }
       if (check.size()!=0) {
           return false;
       }
       return true;
        }
};