class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        print(s)
        #[2,20,4,10,3,4,5] -> {2, 3, 4, 5, 10, 20}
        for num in s:
            if num - 1 not in s:
                current = num
                count = 1

                while current + 1 in s:
                    current += 1
                    count += 1

                longest = max(longest , count)

        return longest 
