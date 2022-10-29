class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lst = str()
        strs= sorted(strs, key=len)
        lst = strs[0]
        for i,j in enumerate(strs[0]):
            for k,l in enumerate(strs):
                if j!=l[i]:
                    return lst[:i]
                
        return lst
    

    #alternative

    class Solution:
    def longestCommonPrefix(self, m):
        if not m: return ''
				#since list of string will be sorted and retrieved min max by alphebetic order
        s1 = min(m)
        s2 = max(m)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i] #stop until hit the split index
        return s1