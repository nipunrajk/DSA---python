#Method 1:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


#Method 2:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            if (i>0 and nums[i-1] == nums[i]):
                return True
        return False

#Method 3:

