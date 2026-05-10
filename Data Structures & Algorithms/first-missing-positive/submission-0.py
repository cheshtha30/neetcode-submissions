class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #find smallest positive integer if any in nums 
        # nums = [-2, -1, 0] -> 0
        #nums[i] +1
        n = len(nums)
        nums.sort()
        expected = 1
        for num in nums:
            if num == expected:
                expected += 1
            else:
               if num > expected:
                break

        return  expected

        