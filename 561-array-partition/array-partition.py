class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Sort the array in ascending order
        nums.sort()
        
        # Step 2: Sum every second element starting from index 0
        # nums[::2] creates a slice containing elements at index 0, 2, 4, ...
        return sum(nums[::2])