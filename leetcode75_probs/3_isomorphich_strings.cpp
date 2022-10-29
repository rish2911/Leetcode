#include <bits/stdc++.h>
using namespace std;
#define MAX_CHARS 256
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int ma[MAX_CHARS];
        memset(ma,-1,sizeof(ma));
        
        bool check[MAX_CHARS] = {false};
        
        for (int i=0;i<s.size();i++) {
            if (ma[s[i]]==-1) {
                if (check[t[i]]==true) {
                    return false;
                }
                
                ma[s[i]]=t[i];
                check[t[i]]=true;
            }
            
            else if (ma[s[i]]!=t[i]) {
                    return false;
                }
         }
        
        
    return true;}
};