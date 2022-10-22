class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
   
        
        a = list(s)
        length = 0
        k =0
        for i in a:
            b = []
            b.append(i)
            for j in range(k,len(a)-1):
                
                if a[j+1] not in b:
                    b.append(a[j+1])
                else:
                    break
            if len(b)>length:
                length = len(b)
            k+=1
        return length

class Set_Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       

        """
        :type s: str
        :rtype: int
        """
   
        charSet = set()
    
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res