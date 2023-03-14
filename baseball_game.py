class Solution:
    def calPoints(self, operations: list[str]) -> int:
        currentScore = []
        for item in operations:
            if item == 'C':
                currentScore.pop()
            elif item == 'D':
                thisScore = int(currentScore[-1]) * 2
                currentScore.append(thisScore)
            elif item == '+':
                thisScore = int(currentScore[-1]) + int(currentScore[-2])
                currentScore.append(thisScore)
            else:
                currentScore.append(int(item))

        return sum(currentScore)

ops = ["5","-2","4","C","D","9","+","+"]
print(Solution().calPoints(ops))