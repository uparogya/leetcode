class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        
        mid_point = len(nums) // 2
        left_subtree = nums[:mid_point]
        right_subtree = nums[mid_point+1:]

        root = TreeNode(nums[mid_point])
        root.left = self.sortedArrayToBST(left_subtree)
        root.right = self.sortedArrayToBST(right_subtree)

        return root

solution = Solution().sortedArrayToBST([-10,-3,0,5,9])
print(solution)