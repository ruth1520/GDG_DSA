class Solution:
    def addDigits(self, num: int) -> int:
        number = str(num)
        while len(number) > 1:
            sumtot = 0                
            for i in number:          
                sumtot += int(i)
            number = str(sumtot)      
        return int(number)

