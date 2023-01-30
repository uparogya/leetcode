class Solution:
    def tribonacci(self, n: int) -> int:
        tribonacciList = [0, 1, 1]
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        
        for i in range(2,n):
            newItem = tribonacciList[i] + tribonacciList[i-1] + tribonacciList[i-2]
            tribonacciList.append(newItem)

        return tribonacciList[-1]

n = 25
print(Solution().tribonacci(n))