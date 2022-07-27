class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        last_index= len(nums) - 1
        first = None
        
        i = last_index -1
        while i>=0:
            if nums[i] < nums[i+1]:
                first = i
                break
            i -= 1
            
        if first == None:
            nums.reverse()
            return
            
        j = last_index
        while j>first:
            if nums[j] > nums[first]:
                [nums[j], nums[first]] = [nums[first], nums[j]]
                break
            j -= 1
           
        start = first + 1
        end = last_index
        while start < end:
            [nums[start], nums[end]] = [nums[end], nums[start]]
            start += 1
            end -= 1
            
