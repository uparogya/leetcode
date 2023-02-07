class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        returnArray = []
        j = n

        for i in range(1,n+1):
            returnArray.append(nums[i-1])
            returnArray.append(nums[j])
            j += 1

        return returnArray

nums = [2,5,1,3,4,7]
n = 3
print(Solution().shuffle(nums,n))