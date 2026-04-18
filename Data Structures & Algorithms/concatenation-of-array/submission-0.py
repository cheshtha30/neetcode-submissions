class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [2*n]
        for i in range(n):
            nums.append(nums[i])
           
        return nums 
        