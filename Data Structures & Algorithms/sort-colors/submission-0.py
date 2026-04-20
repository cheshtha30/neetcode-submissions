class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) 
        for j in range(n):
            i = 0
            while i < n-1:
                if nums[i] >  nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                i += 1
        