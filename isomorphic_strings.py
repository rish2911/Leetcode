class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapp = dict()
        
        for i,j in enumerate(s):
            
            if j in mapp.keys() :
                #Checking for already existing keys
                if mapp[j]!=t[i]:
                    
                    return False
                
            elif t[i] in mapp.values():
                #checking for already exisiting values
                return False
    
                
                
                
            else:
                mapp[j] = t[i]
        
                
        return True


sol = Solution()
s = "badc"
t = "baba"
print(sol.isIsomorphic(s,t))