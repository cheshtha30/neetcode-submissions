class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num , 0) +1

            if hashmap[num] > n//2:
                return num