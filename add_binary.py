class Solution:
    def binaryToDecimal(self, binary: str) -> int:
        decimal = 0
        for index, x in enumerate(binary):
            decimal += int(x) * (2**(len(binary) - index - 1))
        return decimal

    def decimalToBinary(self, decimal: int) -> str:
        remainder = str(decimal%2)
        quotient = int((decimal - int(remainder))/2)
        while quotient > 1:
            remainder = str(quotient%2) + remainder
            quotient = int((quotient - (quotient%2))/2)
        return str(quotient) + remainder

    def addBinary(self, a: str, b: str) -> str:
        # return bin(int(a , 2) + int(b,2))[2:]
        return str(int(self.decimalToBinary(self.binaryToDecimal(a)+self.binaryToDecimal(b))))

a = '10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101'
b = '110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011'
print(Solution().addBinary(a,b))
# 110111101100010011000101110110100000011101000101011001000011011000001100011110011010010011000000000
# binaryToDecimal Works -- decimalToBinary Doesn't :: Hence, used function