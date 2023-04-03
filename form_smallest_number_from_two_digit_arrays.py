class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        newList = []
        
        common = list(set(nums1).intersection(set(nums2)))
        common.sort()
        if len(common) > 0: newList.append(common[0])

        nums1.sort()
        nums2.sort()
        newList.append(int(str(nums1[0]) + str(nums2[0])))
        newList.append(int(str(nums2[0]) + str(nums1[0])))

        newList.sort()
        return newList[0]



nums1 = [3,5,2,6]
nums2 = [3,1,7]
print(Solution().minNumber(nums1,nums2))