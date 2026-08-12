class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = {}
        threshold = len(nums) // 3
        result = []
        
        # Count the frequency of each number
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
        # Collect numbers that exceed the threshold
        for num, count in counts.items():
            if count > threshold:
                result.append(num)
                
        return result
