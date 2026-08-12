class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        res=[]
        candidate1=candidate2=None
        count1=count2=0
        for num in nums:
            if num==candidate1:
                count1+=1
            elif num==candidate2:
                count2+=1
            elif count1==0:
                candidate1=num
                count1=1
            elif count2==0:
                candidate2=num
                count2=1
            else:
                count1-=1
                count2-=1
        for can in [candidate1,candidate2]:
            if nums.count(can)>n//3:
                res.append(can)
        return res