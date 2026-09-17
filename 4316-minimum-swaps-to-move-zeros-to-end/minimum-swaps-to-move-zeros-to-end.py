class Solution(object):
    def minimumSwaps(self, nums):
        c=nums.count(0)
        k=0
        for i in range(len(nums)-1,len(nums)-1-c,-1):
            if nums[i]==0:
                k+=1
        return c-k