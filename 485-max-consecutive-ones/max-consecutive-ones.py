class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        c=0
        max=0
        for i in nums:
            if i ==1:
                c+=1
                if max <= c:
                    max=c
            
            else:
                c=0
        
                
        return max
        