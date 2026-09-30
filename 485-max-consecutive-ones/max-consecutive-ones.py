class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        ans=c=0
        for i in nums:
            if i==1:
                c+=1
            else:
                ans=max(ans,c)
                c=0
        return(max(ans,c))
        
        