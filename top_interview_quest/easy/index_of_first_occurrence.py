class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i,j in enumerate(haystack):
            if (len(haystack)-i)>=len(needle) and needle==haystack[i:i+len(needle)]:
                return i
        return -1