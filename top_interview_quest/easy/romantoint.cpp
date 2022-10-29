#include <vector>
class Solution {
public:
    int romanToInt(string s) {
        int num = 0;
        vector<char> roman{'I','V','X','L','C','D','M'};
        vector<int> number{1,5,10,50,100,500, 1000};
        for (int i=0;i<s.size();i++) {
            auto it = find(roman.begin(),roman.end(),s[i]);
            if (it!=roman.end()) {
                int ind = int(it - roman.begin());
                if (i<s.size()-1) {
                    if ((s[i]=='I') && ((s[i+1]=='V') || (s[i+1]=='X'))) {
                        num-=number[ind];
                        continue;
                    }
                    else if ((s[i]=='X') && ((s[i+1]=='L') || (s[i+1]=='C'))) {
                        num-=number[ind];
                        continue;
                    }
                    else if ((s[i]=='C') && ((s[i+1]=='D') || (s[i+1]=='M'))){
                        num-=number[ind];
                        continue;
                    }
                }         
             num+=number[ind]; }
        }
        
        return num;
        
    }
};



//alternative
int romanToInt(string s) 
{
    unordered_map<char, int> T = { { 'I' , 1 },
                                   { 'V' , 5 },
                                   { 'X' , 10 },
                                   { 'L' , 50 },
                                   { 'C' , 100 },
                                   { 'D' , 500 },
                                   { 'M' , 1000 } };
                                   
   int sum = T[s.back()];
   for (int i = s.length() - 2; i >= 0; --i) 
   {
       if (T[s[i]] < T[s[i + 1]])
       {
           sum -= T[s[i]];
       }
       else
       {
           sum += T[s[i]];
       }
   }
   
   return sum;
}


