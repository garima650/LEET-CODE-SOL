class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        unique=len(set(candyType))

        half=len(candyType)//2
        


        return min(unique,half)
        