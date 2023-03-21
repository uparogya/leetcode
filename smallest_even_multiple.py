class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n%2 == 0 else n*2


n = 5
print(Solution().smallestEvenMultiple(n))