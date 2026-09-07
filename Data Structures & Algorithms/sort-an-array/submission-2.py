class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # for i in range(n):
        #     for j in range(n- i - 1):
        #         if nums[j] > nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]

        # return nums  
        # n = len(nums)
        # for i in range(n):
        #     min_index = i
        #     for j in range(i+1 , n):
        #         if nums[j] < nums[min_index]:
        #             min_index = j

        #     nums[i], nums[min_index] = nums[min_index], nums[i]

        # return nums 
        # [10|,9,1,1,1,2,3,1] check 
        #   j  i 
        #   10> 9
        # [10| 10 1 1 1 2 3 1]
        #    j = -1
        #    nums[0] = 9
        # [9 10 | 1 1 1 2 3 1]
        n  = len(nums)
        for i in range(1 , n):
            current = nums[i]
            j = i-1
            while j >=0 and nums[j]> current:
                nums[j+1] = nums[j]
                j-= 1

            nums[j+1] = current

        return nums 

            
