##TIME LIMIT EXCEEDED
#MAKE THE EXECUTION TIME SHORTER

class Solution:
    def countDigitOne(self, n: int) -> int:
        if(len(str(n))) == 1:
            return 0 if n == 0 else 1
        count = 1
        for index in range(10, n + 1):
            count += str(index).count('1')

        return count

oneCount = Solution().countDigitOne(824883294)
print(oneCount)