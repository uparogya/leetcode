class Solution:

    # DEFINING THE CONSTANTS IN DICTIONARY
    romanIntDict = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

    # THE MAIN CONVERTER
    def romanToInt(self, s: str) -> int:
        thisDict = {}
        total = 0

        for index, x in enumerate(s):
            thisInt = self.romanIntDict[x]
            thisDict[index] = thisInt

        newInt = 0
        for index, x in enumerate(thisDict):
            if(newInt > 0) :
                newInt = 0
                continue

            if index + 1 < len(thisDict):
                if thisDict[index] < thisDict[index+1]:
                    newInt = thisDict[index+1] - thisDict[index]
            if newInt > 0 :
                total += newInt
            else:
                total += thisDict[index]

        return total

# PRE CONVERSION
roman = input("Enter roman number: ")
integer = Solution().romanToInt(roman)
print(integer)