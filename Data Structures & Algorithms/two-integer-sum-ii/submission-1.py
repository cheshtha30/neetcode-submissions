class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        
        for i in range(len(numbers)):
            needed = target - numbers[i]

            if needed in d:
                return [d[needed]+1, i+1]

            d[numbers[i]] = i
        