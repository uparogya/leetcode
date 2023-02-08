class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        if target > nums[-1]: return len(nums)
        if target == nums[-1]: return len(nums) - 1
        if target <= nums[0]: return 0

        while True:
            mid = int((end+start)/2)
            if target == nums[mid]: return mid

            if target < nums[mid+1] and target > nums[mid]: return mid + 1

            if target > nums[mid]: start = mid

            if target < nums[mid]: end = mid

nums = []
target = 1
print(Solution().searchInsert(nums,target))