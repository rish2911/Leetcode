class Solution:
    def isValid(self, s: str) -> bool:
        pair = {"(":")", "[":"]", "{":"}"}
        seq = []
        if len(s)%2!=0:
            return False
        for i,j in enumerate(s):
            if j in pair.keys():
                seq.append(j)
            elif len(seq)>0:
                if j==pair[seq[-1]]:
                    seq.pop()
                    continue
                else :
                    return False
            else:
                return False
        if len(seq)==0:
            return True
        else:
            return False