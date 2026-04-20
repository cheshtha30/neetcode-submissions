from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        n = len(nums)

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

            sortedS =sorted(freq.items(), key = lambda x : x[1], reverse = True)

            result = [item[0] for item in sortedS[:k]]
        return result 


        
        