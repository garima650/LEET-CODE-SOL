class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        x=set(candyType)
        if(len(x)==1):
            return(1)
        elif(len(x)<(len(candyType)/2)):
            return(len(x))
        else:
            return(len(candyType)/2)