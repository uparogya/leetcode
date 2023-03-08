class Solution:
    def leftRigthDifference(self, nums: list[int]) -> list[int]:
        j = len(nums)-1
        currentLeftSum = 0
        currentRightSum = 0
        leftSum = [0]
        rightSum = [0]
        answer = []
        for i in range(0,j):
            currentLeftSum += nums[i]
            currentRightSum += nums[j-i]
            leftSum.append(currentLeftSum)
            rightSum.append(currentRightSum)

        rightSum.reverse()
        
        for i in range(0,j+1):
            answer.append(abs(rightSum[i] - leftSum[i]))

        return answer

nums = [1]
print(Solution().leftRigthDifference(nums))