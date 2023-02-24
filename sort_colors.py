class Solution:
    def sortColors(self, nums: list[int]) -> None:
        countArray = [0,0,0]
        for x in nums:
            if x == 0: countArray[0] += 1
            if x == 1: countArray[1] += 1
            if x == 2: countArray[2] += 1

        count = 0
        for x in range(0,3):
            for y in range(0,countArray[x]):
                nums[count] = x
                count += 1
        
        # print(nums)

# nums = [2,1,0]
# Solution().sortColors(nums)