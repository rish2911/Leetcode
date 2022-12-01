class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]<9:
            digits[-1]+=1
            return digits
        else:
            num = 0
            for i,j in enumerate(digits[::-1]):
                print('i is', i)
                num+=j*(10**(i))
            print(num)
            num=str(num+1)
            new_num = [int(i) for i in num]
            return new_num