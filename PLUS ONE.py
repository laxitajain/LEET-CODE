class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits)==1 and digits[0]==9:
            digits[0]=1
            digits.append(0)
            return digits
        if digits[len(digits)-1]==9:
            for i in range(len(digits)-1,-1,-1):
                digits[i]=0
                if(digits[i-1]!=9):
                    digits[i-1]+=1
                    break
            if digits[len(digits)-1]==1 and all(i==0 for i in digits[0:len(digits)-2]):
                digits.reverse()
                digits.append(0)
                return digits        
            return digits
        digits[len(digits)-1]=digits[len(digits)-1]+1
        return digits
