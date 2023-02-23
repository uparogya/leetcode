class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        finalist = set(nums1).intersection(set(nums2))
        finalist = list(finalist)
        finalist.sort()
        return finalist[0] if len(finalist) > 0 else -1

nums1 = [1,2]
nums2 = [2,4,2]
print(Solution().getCommon(nums1,nums2))