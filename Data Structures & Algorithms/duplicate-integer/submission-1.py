class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                return True      
        return False
        