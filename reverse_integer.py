class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        characters = []
        newChar = ''

        for char in str(x):
            if char == '-':
                neg = True
                continue
            characters.append(char)

        for char in range(len(characters),0,-1):
            char -= 1
            newChar += characters[char]
        
        if neg: newChar = '-' + newChar


        if int(newChar) < -2**31:
            return 0
        elif int(newChar) > (2**31) - 1:
            return 0
        else:
            return int(newChar)

x = 1534236469
print(Solution().reverse(x))