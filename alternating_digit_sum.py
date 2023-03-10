class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sum = 0
        for i, digit in enumerate(str(n)):
            if i%2 == 0: sum += int(digit)
            else: sum += -int(digit)
        
        return sum

n = 1
print(Solution().alternateDigitSum(n))