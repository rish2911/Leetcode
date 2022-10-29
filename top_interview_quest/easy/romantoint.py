class Solution:
    def romanToInt(self, s: str) -> int:
        plan = {'I':1, 'V':5,'X':10,'L':50,'C':100, 'D':500, 'M':1000}
        num = 0
        for i,j in enumerate(s):
                if i<(len(s)-1):
                    if (j=='I') and (s[i+1]=='V' or s[i+1]=='X'):
                        num-=plan[j]
                        continue
                    elif (j=='X') and (s[i+1]=='L' or s[i+1]=='C'):
                        num-=plan[j]
                        continue
                    elif (j=='C') and (s[i+1]=='D' or s[i+1]=='M'):
                        num-=plan[j]
                        continue
                num+=plan[j]
        return num   




##alternative method

class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number