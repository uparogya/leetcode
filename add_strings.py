class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        arr1 = []
        arr2 = []
        output = []
        sum = ''

        for digit in num1:
            arr1.append(int(digit))

        for digit in num2:
            arr2.append(int(digit))

        arr1.reverse()
        arr2.reverse()

        while len(arr1) != len(arr2):
            if(len(arr1) > len(arr2)):
                arr2.append(0)
            else:
                arr1.append(0)
        
        carryOver = 0
        for index, arr1Digit in enumerate(arr1):
            thisSum = arr1Digit + arr2[index] + carryOver
            if(thisSum > 9):
                carryOver = 1
                thisSum -= 10
            else:
                carryOver = 0

            output.append(thisSum)
            if(index+1 == len(arr1) and carryOver == 1):
                output.append(1)
        
        output.reverse()
        for digit in output:
            sum += str(digit)

        return sum

num1 = '19'
num2 = '19'
print(Solution().addStrings(num1,num2))