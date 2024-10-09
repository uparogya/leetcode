class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ""
        while n != 0 or len(binary) != 32:
            binary = str(n%2) + binary
            n = n//2
        
        reversed_bits = self.reverse(binary)
        integer = 0
        for index, bit in enumerate(reversed_bits):
            if int(bit) == 1:
                integer += 2**(31-index)
        
        return integer
    
    def reverse(self, bits: str) -> str:
        if len(bits) == 1:
            return bits
        
        midpoint = len(bits)//2
        left_bits = bits[:midpoint]
        right_bits = bits[midpoint:]
        return str(self.reverse(right_bits)) + str(self.reverse(left_bits))

solution = Solution().reverseBits(43261596)
print(solution)