class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prodTot = 1
        sumTot = 0
        num = str(n)
        for i in num:
            prodTot *= int(i)
            sumTot += int(i)
        return prodTot - sumTot
