class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = ""
        while n != 0:
            binary = str(n%2) + binary
            n = n//2

        return self.countBits(binary)

    def countBits(self, b: str) -> int:
        if b == '1':
            return 1
        elif b == '0' or not b:
            return 0
        mid_point = len(b) // 2
        this_weight = 1 if b[mid_point] == '1' else 0
        left_bits = b[:mid_point]
        right_bits = b[mid_point+1:]
        return this_weight + self.countBits(left_bits) + self.countBits(right_bits)

solution = Solution().hammingWeight(11)
print(solution)