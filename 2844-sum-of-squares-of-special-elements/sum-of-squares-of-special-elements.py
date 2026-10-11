class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        c=0
        j=1
        n=len(nums)
        for i in nums:
            if(n%j==0):
                c=c+i**2
            j+=1
        return(c)   