class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low == high:
            if low%2 == 0: 
                return 0
            else:
                return 1

        if low%2 == 0: low += 1
        if high%2 == 0: high -= 1

        odd = ((high-low)/2) + 1
        return(int(odd))

low = 1
high = 3
print(Solution().countOdds(low,high))