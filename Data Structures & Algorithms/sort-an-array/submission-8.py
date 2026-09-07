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
        # n  = len(nums)
        # for i in range(1 , n):
        #     current = nums[i]
        #     j = i-1
        #     while j >=0 and nums[j]> current:
        #         nums[j+1] = nums[j]
        #         j-= 1

        #     nums[j+1] = current

    #     # return nums 
    #     if len(nums) <= 1:
    #         return nums

    #     mid = len(nums)//2
    #     left= nums[:mid]
    #     right= nums[mid:]

    #     left = self.sortArray(left)
    #     right = self.sortArray(right)
    #     return self.merge(left, right)

    # def merge(self, left, right):
    #     result = []
    #     i = 0
    #     j = 0
    #     while i < len(left) and j < len(right):
    #         if left[i] < right[j]:
    #             result.append(left[i])
    #             i += 1
    #         else:
    #             result.append(right[j])
    #             j +=1

    #     while i < len(left):
    #         result.append(left[i])
    #         i+= 1

    #     while j < len(right):
    #         result.append(right[j])
    #         j+=1

    #     return result 
        if len(nums) <= 1:
            return nums

        left = []
        right = []
        equal = []

        pivot = nums[len(nums)//2]

        for num in nums:
           if num < pivot:
             left.append(num)
           elif num > pivot:
             right.append(num)
           else:
             equal.append(num)

        return self.sortArray(left) + equal + self.sortArray(right)