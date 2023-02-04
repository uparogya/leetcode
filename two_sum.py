class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices = []
        found = False
        for firstIndex, firstItem in enumerate(nums):
            if found == True: break
            for secondIndex in range(firstIndex+1, len(nums)):
                if firstItem + nums[secondIndex] == target:
                    indices.append(firstIndex)
                    indices.append(secondIndex)
                    found = True
                    break

        return indices

nums = [3,3]
target = 6
print(Solution().twoSum(nums,target))