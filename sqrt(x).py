class Solution:
    def mySqrt(self, x: int) -> int:
        oddNumber = 1
        count = 0
        while True:
            if(x < oddNumber): break
            x = x - oddNumber
            count += 1
            oddNumber += 2

        return count
    
x = ((2**31) - 1)
print(Solution().mySqrt(x))