class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      nums.sort()
      for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
      return False
    
      #nums.sort()-> space complexity 0(1)
      #sorted(nums) -> space complexity 0(n)