class Solution(object):
   def findDisappearedNumbers(self, nums):
        allNums = [0] * len(nums)
        for i in nums:
            allNums[i - 1] = i

        return [i + 1 for i in range(len(allNums)) if allNums[i] == 0]