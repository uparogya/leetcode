class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        numString = ''
        newList = []

        for x in digits:
            numString += str(x)

        for x in str(int(numString) + 1):
            newList.append(int(x))

        return newList


digits = [0,1]
print(Solution().plusOne(digits))