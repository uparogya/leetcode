class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes: return k
        if k <= numOnes+numZeros: return numOnes
        return numOnes + ((k-(numOnes+numZeros))*(-1))

numOnes = 2
numZeros = 3
numNegOnes = 3
k = 0
print(Solution().kItemsWithMaximumSum(numOnes,numZeros,numNegOnes,k))